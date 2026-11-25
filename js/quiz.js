// 퀴즈 로직: DOM과 무관한 순수 함수.

// 실제 시험: 10문제 중 O/X 3문제, 나머지 객관식.
export const MOCK_SIZE = 10;
export const MOCK_OX = 3;
export const POINTS_PER_QUESTION = 1;

/** 새 배열로 섞는다(Fisher–Yates). */
export function shuffle(arr, rand = Math.random) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/** 화면에 보일 보기 목록. O/X는 순서 고정, 객관식은 섞는다. */
export function presentChoices(q, rand = Math.random) {
  if (q.type === 'ox') {
    return [
      { text: 'O', isAnswer: q.answer === true },
      { text: 'X', isAnswer: q.answer === false },
    ];
  }
  return shuffle(q.choices.map((text, i) => ({ text, isAnswer: i === q.answer })), rand);
}

export function grade(_q, picked) {
  return Boolean(picked && picked.isAnswer);
}

const byId = (a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0);

/** '나왔다고 함' 주제 이름 목록(문항에 나온 순서대로 중복 없이). */
export function reportedTopics(questions) {
  return [...new Set(questions.map((q) => q.reported).filter(Boolean))];
}

/** 풀 문항 목록을 만든다. kind: 'unit' | 'wrong' | 'reported' | 'mock' */
export function buildSession(kind, { questions, unit, wrongIds = [], rand = Math.random }) {
  if (kind === 'unit') return questions.filter((q) => q.unit === unit).sort(byId);
  if (kind === 'reported') return questions.filter((q) => q.reported).sort(byId);
  if (kind === 'wrong') {
    const want = new Set(wrongIds);
    return shuffle(questions.filter((q) => want.has(q.id)), rand);
  }
  if (kind === 'mock') {
    // 시험과 같은 구성: O/X 3개 + 객관식 7개를 뽑아 섞는다. 한쪽이 모자라면 있는 만큼만.
    // '나왔다고 함' 주제는 주제마다 한 문제씩 먼저 넣고, 나머지를 무작위로 채운다.
    const nOx = Math.min(MOCK_OX, questions.filter((q) => q.type === 'ox').length);
    const want = { ox: nOx, mc: MOCK_SIZE - nOx };
    const picked = [];
    const take = (q) => { picked.push(q); want[q.type] -= 1; };
    for (const topic of reportedTopics(questions)) {
      const pool = shuffle(questions.filter((q) => q.reported === topic && want[q.type] > 0), rand);
      if (pool.length) take(pool[0]);
    }
    for (const type of ['ox', 'mc']) {
      const rest = shuffle(questions.filter((q) => q.type === type && !picked.includes(q)), rand);
      rest.slice(0, Math.max(0, want[type])).forEach(take);
    }
    return shuffle(picked, rand);
  }
  throw new Error('unknown session kind: ' + kind);
}

export function scoreMock(answers) {
  const correct = answers.filter(Boolean).length;
  return { correct, points: correct * POINTS_PER_QUESTION, max: answers.length * POINTS_PER_QUESTION };
}
