import { test } from 'node:test';
import assert from 'node:assert/strict';
import { chartHTML, compareHTML } from '../js/render-extra.js';
import { readFileSync } from 'node:fs';

const cards = JSON.parse(readFileSync(new URL('../data/cards.json', import.meta.url), 'utf8')).cards;

test('every chart renders svg without NaN', () => {
  for (const c of cards.filter((x) => x.chart)) {
    const html = chartHTML(c.chart);
    assert.match(html, /<svg/);
    assert.ok(!html.includes('NaN') && !html.includes('Infinity'), c.id);
    assert.equal(c.chart.x.length, c.chart.y.length, c.id);
  }
});

test('bar chart draws one rect per value', () => {
  const html = chartHTML({ type: 'bar', title: 't', xTitle: 'x', yTitle: 'y', x: ['a', 'b'], y: [3, 5], hi: 1, every: 1 });
  assert.equal((html.match(/<rect/g) || []).length, 2);
  assert.match(html, /cbar hi/);
});

test('compare table escapes html', () => {
  const html = compareHTML({ head: ['a'], rows: [['<b>', 'x']] });
  assert.ok(html.includes('&lt;b&gt;'));
});
