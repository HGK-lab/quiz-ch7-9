// 카드에 들어가는 차트(SVG)와 비교표를 HTML 문자열로 만든다(DOM 불필요).
import { esc } from './render-table.js';

const W = 340, H = 196, L = 40, R = 10, T = 22, B = 40;

function niceMax(v) {
  const p = 10 ** Math.floor(Math.log10(v));
  const f = (v * 1.1) / p;
  return ([1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10].find((c) => c >= f) ?? 10) * p;
}

const fmt = (n) => Number(Number(n).toFixed(2)).toLocaleString('ko-KR');

/** spec: { type: hist|bar|line, title, xTitle, yTitle, x[], y[], hi, every } */
export function chartHTML(spec) {
  const { type, x, y, hi = -1, every = 1 } = spec;
  let top = niceMax(Math.max(...y)), lo = 0;
  if (type === 'line') {
    const mn = Math.min(...y), mx = Math.max(...y);
    const step = 10 ** Math.floor(Math.log10(mx - mn || 1));
    lo = Math.floor(mn / step) * step;
    top = Math.ceil(mx / step) * step;
  }
  const pw = W - L - R, ph = H - T - B;
  const n = x.length;
  const sy = (v) => T + ph - ((v - lo) / (top - lo)) * ph;
  const slot = pw / n;
  const cx = (i) => L + slot * i + slot / 2;
  const parts = [];

  parts.push(`<line class="ax" x1="${L}" y1="${T + ph}" x2="${W - R}" y2="${T + ph}"/>`);
  for (const v of [lo, top]) {
    parts.push(`<text class="yt" x="${L - 6}" y="${sy(v) + 4}" text-anchor="end">${fmt(v)}</text>`);
  }
  parts.push(`<line class="gr" x1="${L}" y1="${sy(top)}" x2="${W - R}" y2="${sy(top)}"/>`);

  if (type === 'line') {
    const pts = y.map((v, i) => `${cx(i).toFixed(1)},${sy(v).toFixed(1)}`).join(' ');
    parts.push(`<polyline class="ln" points="${pts}"/>`);
    if (n <= 12) y.forEach((v, i) => parts.push(`<circle class="dt${i === hi ? ' hi' : ''}" cx="${cx(i).toFixed(1)}" cy="${sy(v).toFixed(1)}" r="${i === hi ? 4.5 : 3}"/>`));
    else parts.push(`<circle class="dt hi" cx="${cx(hi).toFixed(1)}" cy="${sy(y[hi]).toFixed(1)}" r="4.5"/>`);
    parts.push(`<text class="vt" x="${Math.min(Math.max(cx(hi), L + 18), W - R - 18).toFixed(1)}" y="${(sy(y[hi]) - 9).toFixed(1)}" text-anchor="middle">${fmt(y[hi])}</text>`);
  } else {
    const gap = type === 'hist' ? 1.5 : slot * 0.28;
    y.forEach((v, i) => {
      const bx = L + slot * i + gap / 2, bw = slot - gap, by = sy(v);
      parts.push(`<rect class="cbar${i === hi ? ' hi' : ''}" x="${bx.toFixed(1)}" y="${by.toFixed(1)}" width="${bw.toFixed(1)}" height="${(T + ph - by).toFixed(1)}"/>`);
      if (type === 'bar' || i === hi) parts.push(`<text class="vt" x="${(bx + bw / 2).toFixed(1)}" y="${(by - 5).toFixed(1)}" text-anchor="middle">${fmt(v)}</text>`);
    });
  }
  x.forEach((label, i) => {
    if (i % every === 0) parts.push(`<text class="xt" x="${cx(i).toFixed(1)}" y="${T + ph + 15}" text-anchor="middle">${esc(label)}</text>`);
  });
  parts.push(`<text class="at" x="${(L + pw / 2).toFixed(1)}" y="${H - 5}" text-anchor="middle">${esc(spec.xTitle)}</text>`);
  parts.push(`<text class="at" transform="translate(11 ${T + ph / 2}) rotate(-90)" text-anchor="middle">${esc(spec.yTitle)}</text>`);
  return `<figure class="chart"><figcaption>${esc(spec.title)}</figcaption><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(spec.title)}">${parts.join('')}</svg></figure>`;
}

/** { head: [], rows: [[]] } → 표 */
export function compareHTML(t) {
  const head = t.head.map((h) => `<th>${esc(h)}</th>`).join('');
  const rows = t.rows.map((r) => `<tr>${r.map((c, j) => (j === 0 ? `<th scope="row">${esc(c)}</th>` : `<td>${esc(c)}</td>`)).join('')}</tr>`).join('');
  return `<div class="cmp"><table><thead><tr>${head}</tr></thead><tbody>${rows}</tbody></table></div>`;
}
