"""content.py의 내용을 data/*.json으로 만든다.

- 예시: 숨은 준비 코드와 화면 코드를 실제 pandas로 실행해 앞 표와 출력 결과를 얻는다.
- 차트: imdb_top_1000.csv, delivery_orders.csv에서 집계한 숫자만 저장한다(원본 CSV는 저장소에 넣지 않는다).

실행: python -X utf8 tools/build_content.py [데이터폴더]
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from content import CARDS, EXAMPLES, UNITS, QUESTIONS

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\Users\ii076\Desktop\python_learn\Pandas\5장\data")


def table(name: str, df: pd.DataFrame) -> dict:
    return {
        "name": name,
        "columns": [str(c) for c in df.columns],
        "index": [str(i) for i in df.index],
        "rows": [[str(v) for v in row] for row in df.itertuples(index=False)],
    }


def build_example(spec: dict) -> dict:
    ns: dict = {"pd": pd}
    exec(spec["setup"], ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(spec["code"], ns)
    return {
        "id": spec["id"],
        "code": spec["code"],
        "before": [table(n, ns[n]) for n in spec["before"]],
        "after": {"text": buf.getvalue().rstrip()},
    }


def build_charts() -> dict:
    movies = pd.read_csv(DATA / "imdb_top_1000.csv")
    orders = pd.read_csv(DATA / "delivery_orders.csv")
    rating, votes = movies["IMDB_Rating"], movies["No_of_Votes"]

    counts, edges = np.histogram(votes, bins=np.arange(0, 2_400_001, 200_000))
    votes_hist = {"type": "hist", "title": "영화 투표수 분포(구간 너비 20만 표)", "xTitle": "투표수(만 표), 각 구간의 시작값", "yTitle": "영화 수",
                  "x": [f"{e / 10000:.0f}" for e in edges[:-1]], "y": [int(c) for c in counts], "hi": int(np.argmax(counts)), "every": 2}

    bins = np.round(np.arange(7.6, 9.5, 0.2), 1)
    rc, _ = np.histogram(rating, bins=bins)
    rating_hist = {"type": "hist", "title": "영화 평점 분포", "xTitle": "IMDB_Rating", "yTitle": "영화 수",
                   "x": [f"{b:.1f}" for b in bins[:-1]], "y": [int(c) for c in rc], "hi": int(np.argmax(rc)), "every": 1}

    hi, mid, low = (rating >= 9.0).sum(), ((rating >= 8.0) & (rating < 9.0)).sum(), (rating < 8.0).sum()
    rating_bar = {"type": "bar", "title": "평점 구간별 영화 편수", "xTitle": "평점 구간", "yTitle": "영화 편수",
                  "x": ["9.0 이상", "8.0~9.0 미만", "8.0 미만"], "y": [int(hi), int(mid), int(low)], "hi": 2, "every": 1}

    yearly = movies[movies["Released_Year"] != "PG"].groupby("Released_Year")["IMDB_Rating"].mean()
    year_line = {"type": "line", "title": "개봉연도별 평균 평점(Released_Year가 'PG'인 1건 제외)", "xTitle": "개봉연도", "yTitle": "평균 평점",
                 "x": list(yearly.index), "y": [round(float(v), 2) for v in yearly.values], "hi": int(np.argmax(yearly.values)), "every": 20}

    monthly = orders.groupby("주문년월")["주문금액"].mean()
    month_labels = [m[-2:].lstrip("0") + "월" for m in monthly.index]
    monthly_line = {"type": "line", "title": "월별 평균 배달음식 주문금액", "xTitle": "주문년월", "yTitle": "평균 주문금액(원)",
                    "x": month_labels, "y": [round(float(v)) for v in monthly.values], "hi": int(np.argmax(monthly.values)), "every": 1}

    tx = orders.groupby("주문년월")["주문ID"].count()
    monthly_bar = {"type": "bar", "title": "월별 배달음식 주문 횟수", "xTitle": "주문년월", "yTitle": "주문횟수",
                   "x": month_labels, "y": [int(v) for v in tx.values], "hi": int(np.argmax(tx.values)), "every": 1}
    return {"votes_hist": votes_hist, "rating_hist": rating_hist, "rating_bar": rating_bar,
            "year_line": year_line, "monthly_line": monthly_line, "monthly_bar": monthly_bar}


def main() -> None:
    out = ROOT / "data"
    out.mkdir(exist_ok=True)
    charts = build_charts()
    cards = []
    for c in CARDS:
        card = {"id": c["id"], "unit": c["unit"], "title": c["title"], "form": c.get("form"), "body": c["body"],
                "exampleId": c.get("exampleId"), "pages": c["pages"], "lectureOnly": False}
        if "compare" in c:
            card["compare"] = c["compare"]
        if "chart" in c:
            card["chart"] = charts[c["chart"]]
        cards.append(card)
    (out / "cards.json").write_text(json.dumps({"units": UNITS, "cards": cards}, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "examples.json").write_text(json.dumps([build_example(s) for s in EXAMPLES], ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "questions.json").write_text(json.dumps(QUESTIONS, ensure_ascii=False, indent=1), encoding="utf-8")
    print("cards", len(cards), "examples", len(EXAMPLES), "questions", len(QUESTIONS))
    for k, v in charts.items():
        print(k, v["y"][:12], "hi", v["hi"])


if __name__ == "__main__":
    main()
