"""문제은행 정답 검증.

- expect가 있는 문항: code를 실제 pandas로 실행해 출력이 expect와 같은지 확인한다.
  객관식은 정답 보기가 expect와 같아야 한다(loose 문항은 출력만 확인).
- 구조 검사: id 중복 없음, 객관식 보기 4개·정답 번호 범위, 모든 문항에 해설과 쪽 번호.
- 시험 형식: 문제은행에 O/X 3개 이상, 객관식 7개 이상.
- 코드에 px가 들어간 문항은 실행하지 않고(그래프 창) 문법만 검사한다.

실행: python -X utf8 tools/verify.py
"""
import ast
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "data" / "questions.json"


def run_code(code: str) -> str:
    env = {k: v for k, v in os.environ.items()}
    env["PYTHONIOENCODING"] = "utf-8"
    proc = subprocess.run([sys.executable, "-c", "import pandas as pd\n" + code], capture_output=True,
                          text=True, encoding="utf-8", timeout=30, env=env)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else "exit %d" % proc.returncode)
    return proc.stdout.strip()


def verify(q: dict):
    for key in ("explain", "pages", "stem"):
        if not q.get(key):
            return f"{q['id']}: {key} 없음"
    if q["type"] == "mc":
        if len(q["choices"]) != 4 or len(set(q["choices"])) != 4:
            return f"{q['id']}: 보기는 서로 다른 4개여야 함"
        if type(q["answer"]) is not int or not 0 <= q["answer"] < 4:
            return f"{q['id']}: 정답 번호 범위 밖"
    elif q["type"] == "ox":
        if not isinstance(q["answer"], bool):
            return f"{q['id']}: O/X 정답은 bool"
    else:
        return f"{q['id']}: 알 수 없는 유형"
    code = q.get("code")
    expect = q.get("expect")
    if expect is None:
        return None
    if not code:
        return f"{q['id']}: expect가 있는데 code 없음"
    try:
        out = run_code(code)
    except Exception as e:
        return f"{q['id']}: 실행 실패 {e}"
    if out != expect:
        return f"{q['id']}: 출력 {out!r} != expect {expect!r}"
    if q["type"] == "mc" and not q.get("loose") and q["choices"][q["answer"]] != expect:
        return f"{q['id']}: 정답 보기 {q['choices'][q['answer']]!r} != expect {expect!r}"
    if q["type"] == "ox" and f"{expect}" not in q["explain"].replace(",", ""):
        return f"{q['id']}: O/X 해설에 실행 결과 {expect!r}가 없음"
    return None


def syntax_only(q: dict):
    """px 코드(그래프 창을 여는 코드)는 실행하지 않고 문법만 본다. 빈칸(_____)은 대체."""
    code = (q.get("code") or "").replace("_____", "title='t'")
    try:
        ast.parse(code)
    except SyntaxError as e:
        return f"{q['id']}: 코드 문법 오류 {e}"
    return None


def main() -> int:
    qs = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    errors = []
    ids = [q["id"] for q in qs]
    if len(ids) != len(set(ids)):
        errors.append("id 중복")
    ox = sum(q["type"] == "ox" for q in qs)
    mcs = sum(q["type"] == "mc" for q in qs)
    if ox < 3 or mcs < 7:
        errors.append(f"시험 형식 부족: O/X {ox}, 객관식 {mcs}")
    checked = 0
    for q in qs:
        e = verify(q)
        if e is None and q.get("code") and "px." in q["code"]:
            e = syntax_only(q)
        if e:
            errors.append(e)
        elif q.get("expect") is not None:
            checked += 1
    print(f"문항 {len(qs)}개(O/X {ox}, 객관식 {mcs}), 코드 실행 검증 {checked}개")
    for e in errors:
        print("오류:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
