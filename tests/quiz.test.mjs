import { test } from 'node:test';
import assert from 'node:assert/strict';
import { shuffle, presentChoices, grade, buildSession, scoreMock, MOCK_SIZE, MOCK_OX } from '../js/quiz.js';

const seq = (vals) => { let i = 0; return () => vals[i++ % vals.length]; };
const ox = (id, answer, unit = 7) => ({ id, unit, type: 'ox', answer });
const mc = (id, unit = 7) => ({ id, unit, type: 'mc', choices: ['a', 'b', 'c', 'd'], answer: 2 });

test('presentChoices keeps O,X order for ox', () => {
  const r = presentChoices(ox('q', false), seq([0.9, 0.1]));
  assert.deepEqual(r.map((c) => c.text), ['O', 'X']);
  assert.equal(r[1].isAnswer, true);
  assert.equal(r[0].isAnswer, false);
});

test('presentChoices shuffles mc but keeps one answer', () => {
  const r = presentChoices(mc('q'), seq([0.1, 0.2, 0.3]));
  assert.notDeepEqual(r.map((c) => c.text), ['a', 'b', 'c', 'd']);
  assert.equal(r.filter((c) => c.isAnswer).length, 1);
  assert.equal(r.find((c) => c.isAnswer).text, 'c');
});

test('grade reads isAnswer', () => {
  assert.equal(grade(mc('q'), { isAnswer: true }), true);
  assert.equal(grade(mc('q'), { isAnswer: false }), false);
});

test('shuffle returns new array with same items', () => {
  const a = [1, 2, 3, 4];
  const r = shuffle(a, seq([0.5]));
  assert.notEqual(r, a);
  assert.deepEqual([...r].sort(), [1, 2, 3, 4]);
});

test('unit session keeps id order of that unit', () => {
  const qs = [mc('q9-01', 9), mc('q7-02'), mc('q7-01')];
  assert.deepEqual(buildSession('unit', { questions: qs, unit: 7 }).map((q) => q.id), ['q7-01', 'q7-02']);
});

test('mock is 10 questions: 3 ox + 7 mc, all distinct', () => {
  const qs = [
    ...Array.from({ length: 9 }, (_, i) => ox('o' + i, true)),
    ...Array.from({ length: 21 }, (_, i) => mc('m' + i)),
  ];
  for (let k = 0; k < 20; k++) {
    const r = buildSession('mock', { questions: qs });
    assert.equal(r.length, MOCK_SIZE);
    assert.equal(r.filter((q) => q.type === 'ox').length, MOCK_OX);
    assert.equal(r.filter((q) => q.type === 'mc').length, MOCK_SIZE - MOCK_OX);
    assert.equal(new Set(r.map((q) => q.id)).size, MOCK_SIZE);
  }
});

test('mock with too few ox keeps what exists', () => {
  const qs = [ox('o1', true), ...Array.from({ length: 12 }, (_, i) => mc('m' + i))];
  const r = buildSession('mock', { questions: qs });
  assert.equal(r.filter((q) => q.type === 'ox').length, 1);
  assert.equal(r.length, 10);
});

test('wrong session only wrong ids', () => {
  const qs = [mc('a'), mc('b'), mc('c')];
  const r = buildSession('wrong', { questions: qs, wrongIds: ['c', 'a'] });
  assert.deepEqual(r.map((q) => q.id).sort(), ['a', 'c']);
});

test('wrong-only session empty', () => {
  assert.deepEqual(buildSession('wrong', { questions: [mc('a')], wrongIds: [] }), []);
});

test('scoreMock counts correct answers', () => {
  assert.deepEqual(scoreMock([true, false, true]), { correct: 2, points: 2, max: 3 });
});
