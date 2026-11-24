import { test } from 'node:test';
import assert from 'node:assert/strict';
import { esc, exampleHTML } from '../js/render-table.js';
import { readFileSync } from 'node:fs';

const examples = JSON.parse(readFileSync(new URL('../data/examples.json', import.meta.url), 'utf8'));

test('esc escapes html characters', () => {
  assert.equal(esc('<a href="x">&\''), '&lt;a href=&quot;x&quot;&gt;&amp;&#39;');
});

test('every example renders code, before table and output text', () => {
  for (const e of examples) {
    const html = exampleHTML(e);
    assert.match(html, /ex-code/, e.id);
    assert.match(html, /<table>/, e.id);
    assert.match(html, /ex-text/, e.id);
  }
});

test('cards refer to existing examples only', () => {
  const ids = new Set(examples.map((e) => e.id));
  const cards = JSON.parse(readFileSync(new URL('../data/cards.json', import.meta.url), 'utf8')).cards;
  for (const c of cards) if (c.exampleId) assert.ok(ids.has(c.exampleId), c.id);
});
