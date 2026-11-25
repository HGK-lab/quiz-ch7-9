"""7장·9장 내용 원본: 단원, 개념 카드, 예시, 문제.

build_content.py가 이 파일을 읽어 data/*.json을 만든다(예시 표와 차트는 실제 코드와 데이터로 계산).
쪽 번호는 강의자료 슬라이드 번호(슬라이드 오른쪽 아래 숫자)다.
"""

# 다른 학생이 "시험에 나왔다"고 전한 주제(7·9장 범위만). 그 학생 시험과 다를 수 있어 '확정'이 아니라 '나왔다고 함'으로 표시한다.
REPORTED = {
    "nbins": "nbins·구간 너비",
    "bool": "불리언 인덱싱",
    "bar": "px.bar()의 x·y",
    "tail": "tail()",
    "describe": "describe()",
}

UNITS = [
    {"no": 7, "name": "영화 데이터 분석하기"},
    {"no": 9, "name": "Plotly로 시각화하기"},
]

# ---------------------------------------------------------------- 예시
# setup: 숨은 준비 코드, code: 화면에 보이는 코드(실행해서 출력 캡처), before: 앞 표로 보일 변수 이름
MOVIES = (
    "df = pd.DataFrame({\n"
    "    'Series_Title': ['A', 'B', 'C', 'D', 'E', 'F'],\n"
    "    'IMDB_Rating': [8.1, 9.0, 7.6, 8.4, 7.9, 8.8],\n"
    "    'No_of_Votes': [120, 450, 80, 300, 150, 500],\n"
    "})\n"
)
EXAMPLES = [
    {"id": "e_headtail", "setup": MOVIES, "before": ["df"],
     "code": "print(df.head(2))\nprint(df.tail(2))"},
    {"id": "e_shape", "setup": "df = pd.DataFrame({'Title': ['A', 'B', 'C', 'D'], 'Rating': [8.1, 9.0, 7.6, 8.4], 'Votes': [120, 450, 80, 300]})\n",
     "before": ["df"], "code": "print(df.shape)"},
    {"id": "e_describe", "setup": "df = pd.DataFrame({'IMDB_Rating': [7.6, 8.0, 8.4, 9.0, 9.2]})\n",
     "before": ["df"], "code": "print(df['IMDB_Rating'].describe())"},
    {"id": "e_stats", "setup": "df = pd.DataFrame({'IMDB_Rating': [7.6, 8.0, 9.3, 7.6]})\n",
     "before": ["df"], "code": "print(df['IMDB_Rating'].mean())\nprint(df['IMDB_Rating'].max())\nprint(df['IMDB_Rating'].min())"},
    {"id": "e_mask", "setup": "df = pd.DataFrame({'Series_Title': ['A', 'B', 'C', 'D'], 'IMDB_Rating': [8.6, 7.9, 9.0, 8.0]})\n",
     "before": ["df"],
     "code": "max_rating = df['IMDB_Rating'].max()\nmask = df['IMDB_Rating'] == max_rating\nprint(mask)\nprint(df[mask])"},
    {"id": "e_votes", "setup": "df = pd.DataFrame({'No_of_Votes': [120, 80, 300, 500]})\n",
     "before": ["df"], "code": "print(df['No_of_Votes'].sum())\nprint(df['No_of_Votes'].mean())"},
    {"id": "e_range", "setup": "df = pd.DataFrame({'Series_Title': ['A', 'B', 'C', 'D', 'E'], 'IMDB_Rating': [7.8, 8.0, 8.9, 9.0, 8.4]})\n",
     "before": ["df"],
     "code": "mid = df[(df['IMDB_Rating'] >= 8.0) & (df['IMDB_Rating'] < 9.0)]\nprint(mid)\nprint(len(mid))"},
    {"id": "e_groupby_mean", "setup": "df = pd.DataFrame({'주문ID': [1, 2, 3, 4, 5], '주문년월': ['2026-01', '2026-01', '2026-02', '2026-02', '2026-02'], '주문금액': [10000, 20000, 15000, 30000, 15000]})\n",
     "before": ["df"],
     "code": "monthly_amount = df.groupby('주문년월')['주문금액'].mean()\nprint(monthly_amount)\nprint(list(monthly_amount.index))\nprint(list(monthly_amount.values))"},
    {"id": "e_groupby_count", "setup": "df = pd.DataFrame({'주문ID': [1, 2, 3, 4, 5], '주문년월': ['2026-01', '2026-01', '2026-02', '2026-02', '2026-02'], '주문금액': [10000, 20000, 15000, 30000, 15000]})\n",
     "before": ["df"],
     "code": "transactions = df.groupby('주문년월')['주문ID'].count()\nprint(transactions)"},
]

# ---------------------------------------------------------------- 차트(실제 데이터로 계산, build가 채움)
# kind 이름만 적고 값은 build_content.py가 imdb_top_1000.csv, delivery_orders.csv로 만든다.

# ---------------------------------------------------------------- 카드
# body는 문장 목록. form은 코드 상자. compare는 비교표. chart는 build가 만드는 차트 이름.
CARDS = [
    # ----- 7장
    {"id": "c7-01", "unit": 7, "title": "탐색적 데이터 분석(EDA)", "form": None, "pages": "p.2",
     "body": [
         "EDA(Exploratory Data Analysis): 데이터셋을 불러와 각 열의 의미와 값을 정확히 파악하는 과정.",
         "하는 일 세 가지: ① 데이터 구조 이해(각 열이 무엇을 담는지) ② 데이터 품질 확인(결측치, 이상치, 중복값) ③ 패턴과 관계 탐색(변수 사이 관계, 숨은 패턴).",
     ]},
    {"id": "c7-02", "unit": 7, "title": "CSV 파일 불러오기", "form": "df = pd.read_csv('data/imdb_top_1000.csv')\nprint(df)", "pages": "p.3",
     "body": [
         "csv 파일은 pd.read_csv()로 불러와 데이터프레임(df)에 담는다. print(df)로 내용을 출력한다.",
         "IMDB(Internet Movie Database): 미국의 영화 정보 모음 사이트. 이 데이터는 평점 상위 1000편을 담고 있다.",
     ]},
    {"id": "c7-03", "unit": 7, "title": "imdb_top_1000.csv의 열", "form": None, "pages": "p.4",
     "body": ["시험에 자주 쓰는 열을 모았다. 전체 16개 열 중 숫자로 계산하는 열은 IMDB_Rating, Meta_score, No_of_Votes다."],
     "compare": {"head": ["영문 열 이름", "뜻", "설명"], "rows": [
         ["Series_Title", "작품 제목", "영화 또는 시리즈 이름"],
         ["Released_Year", "개봉연도", "작품이 공개된 해"],
         ["Runtime", "상영시간", "작품 길이, 분 단위"],
         ["IMDB_Rating", "IMDb 평점", "이용자 평가 점수, 0~10"],
         ["Meta_score", "메타스코어", "평론가 리뷰 점수(Metacritic)"],
         ["No_of_Votes", "투표수", "평점을 매긴 이용자 수"],
         ["Gross", "흥행수익", "박스오피스 매출, 달러 단위"],
     ]}},
    {"id": "c7-04", "unit": 7, "reported": "tail", "title": "head()와 tail()", "form": "df.head()    # 처음 5행\ndf.tail()    # 마지막 5행\ndf.head(3)   # 처음 3행", "pages": "p.5", "exampleId": "e_headtail",
     "body": [
         "head(): 데이터프레임의 처음 5행을 본다. tail(): 마지막 5행을 본다.",
         "괄호 안에 숫자를 넣으면 그 개수만큼 보여 준다. 숫자가 없으면 5개가 기본이다.",
         "tail(2)는 마지막 두 행이다. 행 번호(인덱스)는 처음부터 매긴 번호 그대로 나온다. 예를 들어 행이 6개(인덱스 0~5)라면 tail(2)는 인덱스 4, 5다.",
         "행이 5개보다 적으면 tail()은 있는 행을 모두 보여 준다.",
     ]},
    {"id": "c7-05", "unit": 7, "reported": "describe", "title": "describe()와 shape", "form": "df.describe()   # 메서드: 괄호 있음\ndf.shape        # 속성: 괄호 없음", "pages": "p.6", "exampleId": "e_shape",
     "body": [
         "describe(): 수치형 열의 기본 통계(개수, 평균, 표준편차, 최솟값, 25%·50%·75%, 최댓값)를 한 번에 본다.",
         "shape: 행과 열의 개수를 (행, 열) 튜플로 알려 준다. 속성이므로 괄호를 붙이지 않는다.",
         "imdb_top_1000.csv의 shape은 (1000, 16)이다.",
     ]},
    {"id": "c7-06", "unit": 7, "reported": "describe", "title": "describe() 결과 읽기", "form": None, "pages": "p.6", "exampleId": "e_describe",
     "body": [
         "count 개수, mean 평균, std 표준편차, min 최솟값, 25%·50%·75% 사분위수, max 최댓값. 50%는 중앙값이다.",
         "문자열 열은 계산할 수 없으므로 기본으로는 수치형 열만 나온다.",
     ]},
    {"id": "c7-07", "unit": 7, "title": "평균·최대·최소 구하기", "form": "df['IMDB_Rating'].mean()   # 평균\ndf['IMDB_Rating'].max()    # 최대\ndf['IMDB_Rating'].min()    # 최소", "pages": "p.8, 11", "exampleId": "e_stats",
     "body": [
         "열 하나를 df['열이름']으로 꺼낸 뒤 mean(), max(), min()을 붙인다.",
         "강의 결과: 평균 평점 약 7.95, 최고 평점 9.3(The Shawshank Redemption), 최저 평점 7.6.",
     ]},
    {"id": "c7-08", "unit": 7, "reported": "bool", "title": "불리언 인덱싱", "form": "max_rating = df['IMDB_Rating'].max()\nmask = df['IMDB_Rating'] == max_rating   # 1단계 조건 검사\nbest = df[mask]                          # 2단계 필터링", "pages": "p.9–10", "exampleId": "e_mask",
     "body": [
         "불리언 인덱싱: 조건을 만족하는 행만 고르는 방법. ① 조건 검사로 True/False로 된 Series(마스크)를 만들고 ② df[마스크]로 True인 행만 뽑는다.",
         "같은지 비교할 때는 ==(두 개)를 쓴다. =(한 개)는 대입이라 오류가 난다.",
         "열 몇 개만 보려면 best[['Series_Title', 'IMDB_Rating']]처럼 이중 대괄호를 쓴다.",
         "마스크 자체(df['IMDB_Rating'] == max_rating)는 행이 아니라 True/False로 된 Series다. df[...]로 감싸야 행이 뽑힌다.",
     ]},
    {"id": "c7-09", "unit": 7, "title": "최저 평점 영화와 len()", "form": "min_rating = df['IMDB_Rating'].min()\nlowest = df[df['IMDB_Rating'] == min_rating]\nlen(lowest)", "pages": "p.11, 13",
     "body": [
         "최고 평점과 같은 방법으로 최솟값을 구하고 같은 평점의 행을 고른다.",
         "같은 평점이 여러 편이면 모두 뽑힌다. 강의 결과: 최저 평점 7.6을 받은 영화는 총 123편.",
         "len(결과)는 뽑힌 행의 개수(영화 편수)다.",
     ]},
    {"id": "c7-10", "unit": 7, "title": "투표수 합계와 평균", "form": "total_votes = df['No_of_Votes'].sum()\naverage_votes = df['No_of_Votes'].mean()", "pages": "p.12–13", "exampleId": "e_votes",
     "body": [
         "sum(): 전체 투표 수(대중적인 인기). mean(): 영화 한 편당 평균 투표 수(평가의 신뢰도 파악에 도움).",
         "강의 결과: 전체 참여자 수 273,692,911명, 영화당 평균 약 273,692명.",
     ]},
    {"id": "c7-11", "unit": 7, "reported": "bool", "title": "조건 두 개 합치기: &", "form": "mid = df[(df['IMDB_Rating'] >= 8.0) & (df['IMDB_Rating'] < 9.0)]", "pages": "p.18", "exampleId": "e_range",
     "body": [
         "두 조건을 모두 만족하는 행: 각 조건을 괄호로 묶고 &로 잇는다. 하나라도 만족하면 |(OR).",
         "Series에는 and, or를 쓰지 않는다.",
         "평점 구간별 편수는 len()으로 센다. 강의 결과: 9.0 이상 5편, 8.0~9.0 미만 458편, 8.0 미만 537편.",
     ]},
    {"id": "c7-12", "unit": 7, "title": "그래프 ①: 투표수 분포(히스토그램)", "form": "fig = px.histogram(df, x='No_of_Votes', nbins=20, title='...')\nfig.show()", "pages": "p.15–16", "chart": "votes_hist",
     "body": [
         "목표: 영화별 투표수가 어떤 범위에 많이 분포하는지 확인.",
         "해석: 대부분 영화가 투표수 50만 표 미만에 몰려 있다. 가장 빈도가 높은 구간은 약 0~20만 표. 투표수가 커질수록 영화 수가 줄고, 일부 영화만 100만 표 이상이다.",
     ]},
    {"id": "c7-13", "unit": 7, "reported": "bar", "title": "그래프 ②: 평점 구간별 편수(막대)", "form": "ratings = ['9.0 이상', '8.0~9.0 미만', '8.0 미만']\ncounts = [len(high), len(mid), len(low)]\nfig = px.bar(x=ratings, y=counts, title='...',\n             labels={'x': '평점 구간', 'y': '영화 편수'})", "pages": "p.17–18", "chart": "rating_bar",
     "body": [
         "목표: 평점 구간별 영화 편수 비교(불리언 인덱싱과 len() 활용).",
         "x에는 막대 이름인 평점 구간을, y에는 막대 높이인 영화 편수를 넣는다.",
         "해석: 8.0 미만이 가장 많고 8.0~9.0 미만이 그다음. 9.0 이상은 매우 적어 큰 차이가 난다.",
     ]},
    {"id": "c7-14", "unit": 7, "title": "그래프 ③: 연도별 평균 평점(꺾은선)", "form": "yearly_rating = df.groupby('Released_Year')['IMDB_Rating'].mean()\nfig = px.line(yearly_rating, x=yearly_rating.index, y=yearly_rating.values)", "pages": "p.19–20", "chart": "year_line",
     "body": [
         "목표: 개봉연도에 따른 평균 평점의 변화. groupby()와 mean()으로 연도별 평균을 구한다.",
         "해석: 대체로 7.8~8.2점 사이에서 오르내리고 뚜렷한 상승·하락 추세는 없다. 1936년이 약 8.5점으로 가장 높다. 최근 연도는 변동 폭이 작다.",
     ]},

    # ----- 9장
    {"id": "c9-01", "unit": 9, "title": "Plotly란", "form": None, "pages": "p.3",
     "body": [
         "Plotly: 웹 친화적이고 인터랙티브한 그래프를 만드는 라이브러리. HTML, CSS, JavaScript 기반이라 웹 환경에 최적화돼 있다.",
         "기능: 줌(특정 영역 확대·축소), 이동(확대한 채 드래그), 툴팁(점에 올리면 값 표시), 데이터 필터링(슬라이더·드롭다운·버튼), 실시간 업데이트.",
     ]},
    {"id": "c9-02", "unit": 9, "title": "시각화 라이브러리 비교", "form": None, "pages": "p.1",
     "body": ["세 라이브러리는 용도가 다르다. 표의 한 줄 특징만 기억하자."],
     "compare": {"head": ["라이브러리", "특징", "적합한 상황"], "rows": [
         ["Plotly", "대화형(줌·툴팁), 코드 직관적. 설치 용량 큼", "발표·보고용, 웹서비스, 프로젝트"],
         ["Matplotlib", "가장 기본, 세밀한 조정 가능. 코드 길고 기본 스타일 투박", "시각화 원리 학습, 논문·학술용 정적 그래프"],
         ["Seaborn", "Matplotlib 기반, 코드 간결, 기본 테마 예쁨. 자유도 낮음", "간단한 통계 그래프, 수업용"],
     ]}},
    {"id": "c9-03", "unit": 9, "title": "plotly.express 불러오기", "form": "import plotly.express as px", "pages": "p.4",
     "body": [
         "plotly.express: 간결하고 직관적인 문법으로 복잡한 설정 없이 다양한 그래프를 만든다. 보통 px라는 이름으로 불러온다.",
         "구글 코랩에는 Plotly가 기본으로 들어 있다. 특정 버전을 쓰고 싶을 때만 설치 명령어(예: Plotly 5.22.0)를 쓴다.",
     ]},
    {"id": "c9-04", "unit": 9, "title": "히스토그램이란", "form": None, "pages": "p.5",
     "body": [
         "히스토그램: 데이터를 일정한 구간(bin)으로 나누고, 각 구간에 속한 데이터의 개수(빈도)를 막대 높이로 나타낸 그래프. 주로 연속형 데이터에 쓴다.",
         "알 수 있는 것: 데이터 분포, 최빈값(가장 높은 막대 구간), 범위(퍼진 정도), 특별한 값(이상치), 치우친 방향.",
     ]},
    {"id": "c9-05", "unit": 9, "reported": "nbins", "title": "px.histogram()", "form": "fig = px.histogram(df, x='IMDB_Rating', nbins=20, title='영화 평점 분포')\nfig.show()", "pages": "p.6–9",
     "body": [
         "df: 데이터프레임, x: X축 열, nbins: 구간 개수(기본값 10), title: 그래프 제목.",
         "fig.show(): 만든 그래프(fig 객체)를 화면에 그린다.",
         "구간 개수 변경하기(p.8): nbins 값으로 조절한다. 구간 개수가 많을수록 세밀한 데이터 분포를 확인할 수 있다.",
         "구간 너비 = (최댓값 − 최솟값) ÷ nbins. 예: 최솟값 7.0, 최댓값 9.0, nbins=20이면 (9.0 − 7.0) ÷ 20 = 0.1.",
     ]},
    {"id": "c9-06", "unit": 9, "title": "평점 히스토그램 읽기", "form": None, "pages": "p.7", "chart": "rating_hist",
     "body": [
         "분포: 대부분 7.6~8.6점 사이. 최빈 구간: 7.6~7.8점. 범위: 약 7.6~9.4점.",
         "특징: 9.0점 이상의 높은 평점을 받은 영화는 상대적으로 적다.",
     ]},
    {"id": "c9-07", "unit": 9, "title": "Plotly 도구 모음", "form": None, "pages": "p.11",
     "body": ["그래프 오른쪽 위에 도구가 나타난다. 이름과 기능을 짝지어 외운다."],
     "compare": {"head": ["도구", "모양", "기능"], "rows": [
         ["Download plot as a png", "카메라", "그래프를 PNG 파일로 저장"],
         ["Zoom", "돋보기", "특정 부분 확대"],
         ["Pan", "손바닥", "상하좌우로 이동"],
         ["Box Select", "사각형", "특정 영역을 선택해 강조"],
         ["Lasso Select", "올가미", "불규칙한 영역 선택, 복잡한 데이터에 사용"],
         ["Zoom in / Zoom out", "확대/축소", "점진적으로 확대·축소"],
         ["Autoscale", "화살표 회전", "데이터 범위에 맞게 축 자동 조정"],
         ["Reset Axes", "집", "그래프를 처음 상태로 복원"],
     ]}},
    {"id": "c9-08", "unit": 9, "title": "배달 주문 데이터", "form": "df = pd.read_csv('data/delivery_orders.csv')\nprint(df.head(3))\nprint(df.tail(3))\nprint(df.info())", "pages": "p.13–14",
     "body": [
         "열: 주문ID, 주문일자, 주문년월(예: 2026-01), 음식종류, 주문금액. 240행 × 5열.",
         "head(3), tail(3)으로 앞뒤를 보고 info()로 열 이름·개수·타입을 확인한다.",
     ]},
    {"id": "c9-09", "unit": 9, "title": "groupby()로 월별 평균", "form": "monthly_amount = df.groupby('주문년월')['주문금액'].mean()\nmonthly_amount.index    # 주문년월\nmonthly_amount.values   # 평균 주문금액", "pages": "p.15", "exampleId": "e_groupby_mean",
     "body": [
         "groupby('주문년월'): 주문년월 열을 기준으로 묶는다. ['주문금액'].mean(): 묶음마다 평균 주문금액을 계산한다.",
         "결과 Series의 .index는 묶은 기준 값(월), .values는 계산된 값(평균 금액)이다. 그래프의 X축은 index, Y축은 values로 쓴다.",
     ]},
    {"id": "c9-10", "unit": 9, "title": "px.line(): 꺾은선그래프", "form": "fig = px.line(monthly_amount,\n               x=monthly_amount.index,\n               y=monthly_amount.values,\n               title='월별 평균 배달음식 주문금액')\nfig.show()", "pages": "p.16–17",
     "body": [
         "꺾은선그래프: 연속적인 데이터를 시간이나 순서에 따라 나타낼 때 쓴다. 함수는 line().",
         "x: X축 데이터, y: Y축 데이터, title: 제목.",
     ]},
    {"id": "c9-11", "unit": 9, "title": "월별 평균 주문금액 읽기", "form": None, "pages": "p.18", "chart": "monthly_line",
     "body": ["볼 것 네 가지: 전체 변화 추세, 평균 주문금액이 가장 높은 달, 가장 낮은 달, 월별 변동.", "이 데이터에서는 3월이 가장 높고 2월이 가장 낮다."]},
    {"id": "c9-12", "unit": 9, "title": "count()로 월별 주문 횟수", "form": "transactions = df.groupby('주문년월')['주문ID'].count()", "pages": "p.20", "exampleId": "e_groupby_count",
     "body": ["count(): 묶음마다 값의 개수(주문 횟수)를 센다. 금액이 아니라 주문ID를 세는 것이 포인트다."],
     "compare": {"head": ["메서드", "하는 일", "예"], "rows": [
         ["mean()", "묶음마다 평균", "월별 평균 주문금액"],
         ["sum()", "묶음마다 합계", "월별 총 주문금액"],
         ["count()", "묶음마다 개수", "월별 주문 횟수"],
     ]}},
    {"id": "c9-13", "unit": 9, "reported": "bar", "title": "px.bar(): 막대그래프", "form": "fig = px.bar(transactions,\n              x=transactions.index,\n              y=transactions.values,\n              title='월별 배달음식 주문 횟수',\n              labels={'x': '주문년월', 'y': '주문횟수'})\nfig.show()", "pages": "p.21–22", "chart": "monthly_bar",
     "body": [
         "막대그래프: 범주형 데이터의 크기·빈도를 비교한다. 크기는 막대 길이(높이).",
         "x=transactions.index(주문년월, 막대 이름), y=transactions.values(주문 횟수, 막대 높이). index와 values는 속성이라 괄호가 없다.",
         "labels는 X축·Y축 이름을 지정하는 딕셔너리(중괄호)다. 리스트나 title이 아니다.",
     ]},
    {"id": "c9-14", "unit": 9, "title": "어떤 그래프를 쓸까", "form": None, "pages": "p.5, 16, 21",
     "body": ["분석 목적으로 그래프를 고른다."],
     "compare": {"head": ["목적", "그래프", "함수"], "rows": [
         ["값의 분포, 구간별 빈도", "히스토그램", "px.histogram()"],
         ["시간·순서에 따른 변화", "꺾은선", "px.line()"],
         ["범주별 크기·횟수 비교", "막대", "px.bar()"],
     ]}},
]

# ---------------------------------------------------------------- 문제
# type: ox | mc. mc는 choices와 answer(0부터). expect가 있으면 code를 실행해 같은지 검증한다.
# loose: 정답 보기 문장이 출력과 달라도 되는 경우.
def ox(id, unit, stem, answer, explain, pages, code=None, expect=None, reported=None):
    q = {"id": id, "unit": unit, "type": "ox", "stem": stem, "code": code, "answer": answer,
         "explain": explain, "pages": pages, "lectureOnly": False, "expect": expect}
    if reported:
        q["reported"] = reported
    return q


def mc(id, unit, stem, choices, answer, explain, pages, code=None, expect=None, loose=False, reported=None):
    q = {"id": id, "unit": unit, "type": "mc", "stem": stem, "code": code, "choices": choices, "answer": answer,
         "explain": explain, "pages": pages, "lectureOnly": False, "expect": expect}
    if loose:
        q["loose"] = True
    if reported:
        q["reported"] = reported
    return q


QUESTIONS = [
    # ===== 7장 =====
    ox("q7-01", 7, "탐색적 데이터 분석(EDA)에서는 데이터 구조를 이해하고, 결측치·이상치·중복값을 확인하고, 변수 사이의 패턴을 찾는다.", True,
       "EDA의 세 가지 주요 작업이다: 구조 이해, 품질 확인(결측치·이상치·중복값), 패턴·관계 탐색.", "p.2"),
    ox("q7-02", 7, "df.shape는 속성이 아니라 메서드이므로 df.shape()처럼 괄호를 붙여 호출해야 한다.", False,
       "shape는 속성이다. 괄호 없이 df.shape로 쓰고, 결과는 (행, 열) 튜플이다. 괄호를 붙이면 튜플을 호출하려 해서 오류가 난다.", "p.6"),
    ox("q7-03", 7, "head()와 tail()에 숫자를 넣지 않으면 각각 처음 5행, 마지막 5행을 보여 준다.", True,
       "head()와 tail()의 기본값은 5행이다. head(3)처럼 숫자를 넣으면 그 개수만큼 본다.", "p.5", reported="tail"),
    ox("q7-04", 7, "불리언 인덱싱은 먼저 조건 검사로 True/False Series를 만들고, 그다음 True인 행만 걸러 내는 순서로 이루어진다.", True,
       "1단계 조건 검사로 불리언 마스크를 만들고, 2단계 df[마스크]로 True인 행만 추출한다.", "p.9", reported="bool"),
    ox("q7-05", 7, "다음 코드의 출력은 2이다.", True,
       "평점이 8.0인 행은 인덱스 0과 2, 두 행이므로 len의 결과는 2이다.", "p.9–10, 18",
       code="df = pd.DataFrame({'IMDB_Rating': [8.0, 9.0, 8.0, 7.5]})\nprint(len(df[df['IMDB_Rating'] == 8.0]))", expect="2", reported="bool"),
    mc("q7-06", 7, "'data/movies.csv' 파일을 데이터프레임으로 불러오는 올바른 코드는?",
       ["df = pd.read_csv('data/movies.csv')", "df = pd.load_csv('data/movies.csv')", "df = pd.read_excel('data/movies.csv')", "df = df.to_csv('data/movies.csv')"], 0,
       "csv 파일은 pd.read_csv()로 읽는다. read_excel은 엑셀용, to_csv는 파일로 저장하는 메서드다. pd.load_csv는 없다.", "p.3"),
    mc("q7-07", 7, "수치형 열의 개수, 평균, 표준편차, 최솟값, 사분위수, 최댓값을 한 번에 보여 주는 메서드는?",
       ["describe()", "head()", "tail()", "shape"], 0,
       "describe()가 기본 통계 정보를 한꺼번에 보여 준다. head·tail은 행 확인용, shape은 크기 확인용이다.", "p.6", reported="describe"),
    mc("q7-08", 7, "다음 코드의 실행 결과는?",
       ["(4, 3)", "(3, 4)", "(4, 4)", "(3, 3)"], 0,
       "shape은 (행, 열) 순서다. 행이 4개, 열이 3개이므로 (4, 3)이다.", "p.6",
       code="df = pd.DataFrame({\n    'Title': ['A', 'B', 'C', 'D'],\n    'Rating': [7.5, 8.5, 9.0, 7.0],\n    'Votes': [120, 80, 300, 500]\n})\nprint(df.shape)", expect="(4, 3)"),
    mc("q7-09", 7, "다음 코드의 실행 결과는?",
       ["8.0", "7.5", "8.5", "32.0"], 0,
       "mean()은 평균이다. (7.5 + 8.5 + 9.0 + 7.0) ÷ 4 = 8.0. 32.0은 sum()의 결과다.", "p.8",
       code="df = pd.DataFrame({'IMDB_Rating': [7.5, 8.5, 9.0, 7.0]})\nprint(df['IMDB_Rating'].mean())", expect="8.0"),
    mc("q7-10", 7, "영화 전체의 투표 수 합계를 구하는 올바른 코드는?",
       ["df['No_of_Votes'].sum()", "df['No_of_Votes'].mean()", "df['No_of_Votes'].max()", "df['No_of_Votes'].shape"], 0,
       "합계는 sum()이다. mean()은 영화당 평균 투표 수, max()는 가장 많은 투표 수다.", "p.12"),
    mc("q7-11", 7, "다음 코드의 실행 결과를 올바르게 설명한 것은?",
       ["인덱스 0과 2만 True이다.", "인덱스 0, 2, 3이 True이다.", "인덱스 1만 True이다.", "모든 행이 True이다."], 0,
       "> 8.0은 8.0보다 '큰' 값만 True다. 8.6(인덱스 0)과 9.0(인덱스 2)만 True이고 8.0(인덱스 3)은 False다.", "p.9–10",
       code="df = pd.DataFrame({'IMDB_Rating': [8.6, 7.9, 9.0, 8.0]})\nprint(df['IMDB_Rating'] > 8.0)",
       expect="0     True\n1    False\n2     True\n3    False\nName: IMDB_Rating, dtype: bool", loose=True, reported="bool"),
    mc("q7-12", 7, "평점이 가장 낮은 영화를 모두 추출하는 올바른 코드는?",
       ["min_rating = df['IMDB_Rating'].min()\ndf[df['IMDB_Rating'] == min_rating]",
        "min_rating = df['IMDB_Rating'].min()\ndf[df['IMDB_Rating'] = min_rating]",
        "df['IMDB_Rating'].min()",
        "df[df['IMDB_Rating'] == df['IMDB_Rating'].max()]"], 0,
       "최솟값을 구하고 ==로 같은지 비교해 True인 행만 뽑는다. =은 대입이라 오류, min()만 쓰면 값 하나뿐이고, max()와 비교하면 최고 평점 영화가 나온다.", "p.11", reported="bool"),
    mc("q7-13", 7, "다음 코드의 실행 결과는?",
       ["3", "1", "2", "5"], 0,
       "최저 평점은 7.6이고 7.6인 영화는 3편(인덱스 0, 2, 3)이므로 len(result)는 3이다.", "p.11",
       code="df = pd.DataFrame({'IMDB_Rating': [7.6, 8.1, 7.6, 7.6, 8.8]})\nmin_rating = df['IMDB_Rating'].min()\nresult = df[df['IMDB_Rating'] == min_rating]\nprint(len(result))", expect="3", reported="bool"),
    mc("q7-14", 7, "다음 코드의 실행 결과는?",
       ["3", "2", "4", "6"], 0,
       "8.0 이상이고 9.0 미만인 값은 8.0, 8.9, 8.4로 3개다. 9.0은 '미만' 조건에서 빠진다.", "p.18",
       code="df = pd.DataFrame({'IMDB_Rating': [7.8, 8.0, 8.9, 9.0, 8.4, 9.3]})\nmid = df[(df['IMDB_Rating'] >= 8.0) & (df['IMDB_Rating'] < 9.0)]\nprint(len(mid))", expect="3", reported="bool"),
    mc("q7-15", 7, "영화 투표수 히스토그램에서 0~20만 표 구간의 막대가 가장 높았다. 올바른 해석은?",
       ["투표수가 적은 영화가 많고, 투표수가 커질수록 영화 수가 줄어든다.",
        "모든 영화의 투표수가 20만 표이다.",
        "투표수가 많을수록 영화 수도 늘어난다.",
        "투표수가 가장 많은 영화는 20만 표를 받았다."], 0,
       "막대 높이는 구간에 속한 영화 수다. 0~20만 구간이 가장 높고 오른쪽으로 갈수록 낮아지므로 투표수가 적은 영화가 대부분이다.", "p.15–16"),

    # ----- 나왔다고 함: 불리언 인덱싱, tail(), 막대 x·y
    mc("q7-16", 7, "다음 코드의 실행 결과는?",
       ["['B', 'D']", "['B', 'C', 'D']", "['A', 'C', 'E']", "['D']"], 0,
       "조건 >= 8.5를 만족하는 행은 B(8.8)와 D(9.1)다. 8.5 '이상'이므로 8.4인 C는 빠진다.", "p.9–10",
       code="df = pd.DataFrame({\n    'Series_Title': ['A', 'B', 'C', 'D', 'E'],\n    'IMDB_Rating': [7.9, 8.8, 8.4, 9.1, 8.0]\n})\nresult = df[df['IMDB_Rating'] >= 8.5]\nprint(list(result['Series_Title']))",
       expect="['B', 'D']", reported="bool"),
    mc("q7-17", 7, "다음 코드를 실행했을 때 mask에 들어 있는 것은?",
       ["행마다 True/False가 들어 있는 Series", "최고 평점을 받은 영화의 행들", "최고 평점 값 하나", "오류가 나서 아무것도 없다"], 0,
       "조건 검사의 결과는 행마다 True/False인 Series(마스크)다. 영화 행을 뽑으려면 df[mask]로 한 번 더 걸러야 한다.", "p.9–10",
       code="max_rating = df['IMDB_Rating'].max()\nmask = df['IMDB_Rating'] == max_rating", reported="bool"),
    mc("q7-18", 7, "다음 코드에서 출력되는 행의 인덱스는?",
       ["4, 5", "0, 1", "3, 4, 5", "1, 2"], 0,
       "tail(2)는 마지막 두 행이다. 행이 6개이고 인덱스는 0부터 5까지이므로 인덱스 4, 5가 나온다. 0, 1은 head(2)의 결과다.", "p.5",
       code="df = pd.DataFrame({\n    'A': [10, 20, 30, 40, 50, 60],\n    'B': [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]\n})\nprint(df.tail(2))",
       expect="A    B\n4  50  5.5\n5  60  6.5", loose=True, reported="tail"),
    ox("q7-19", 7, "행이 4개인 데이터프레임에 df.tail()을 실행하면 4행이 모두 나온다.", True,
       "tail()의 기본값은 5행이지만 행이 4개뿐이면 있는 4행을 모두 보여 준다. 아래 코드의 출력은 4이다.", "p.5",
       code="df = pd.DataFrame({'A': [1, 2, 3, 4]})\nprint(len(df.tail()))", expect="4", reported="tail"),
    mc("q7-20", 7, "다음 코드로 평점 구간별 편수 막대그래프를 그린다. 막대의 높이를 정하는 것은?",
       ["y에 넣은 counts", "x에 넣은 ratings", "title", "labels"], 0,
       "px.bar()에서 x는 막대 이름(평점 구간), y는 막대 높이(영화 편수)다. title은 제목, labels는 축 이름이다.", "p.17–18",
       code="ratings = ['9.0 이상', '8.0~9.0 미만', '8.0 미만']\ncounts = [len(high), len(mid), len(low)]\nfig = px.bar(x=ratings, y=counts, title='평점 구간별 영화 편수')", reported="bar"),
    ox("q7-21", 7, "describe()는 메서드이므로 df.describe()처럼 괄호를 붙여 호출한다.", True,
       "describe()는 메서드라 괄호를 붙인다. 괄호를 붙이지 않는 것은 속성인 shape이다.", "p.6", reported="describe"),
    ox("q7-22", 7, "문자열 열과 수치형 열이 함께 있는 데이터프레임에 describe()를 실행하면, 기본으로 수치형 열의 통계만 나온다.", True,
       "문자열은 평균·표준편차를 계산할 수 없으므로 기본 describe()는 수치형 열만 보여 준다.", "p.6", reported="describe"),
    mc("q7-23", 7, "describe() 결과에서 중앙값을 나타내는 행은?",
       ["50%", "mean", "std", "count"], 0,
       "50%는 데이터를 크기순으로 늘어놓았을 때 가운데 값, 곧 중앙값이다. mean은 평균, std는 표준편차, count는 개수다.", "p.6", reported="describe"),
    mc("q7-24", 7, "다음 코드의 출력에서 mean 행의 값은?",
       ["8.44", "8.40", "9.20", "5.00"], 0,
       "mean은 평균이다. (7.6 + 8.0 + 8.4 + 9.0 + 9.2) ÷ 5 = 8.44. 8.40은 50%(중앙값), 9.20은 max, 5.00은 count다.", "p.6",
       code="df = pd.DataFrame({'IMDB_Rating': [7.6, 8.0, 8.4, 9.0, 9.2]})\nprint(df['IMDB_Rating'].describe())",
       expect="count    5.000000\nmean     8.440000\nstd      0.669328\nmin      7.600000\n25%      8.000000\n50%      8.400000\n75%      9.000000\nmax      9.200000\nName: IMDB_Rating, dtype: float64",
       loose=True, reported="describe"),

    # ===== 9장 =====
    ox("q9-01", 9, "Plotly로 만든 그래프는 마우스로 확대·이동하거나 점 위에 올려 값을 볼 수 있다.", True,
       "Plotly는 줌, 이동, 툴팁 같은 상호작용을 지원하는 대화형 시각화 라이브러리다.", "p.3"),
    ox("q9-02", 9, "히스토그램에서 막대의 높이는 그 구간에 속한 데이터의 개수(빈도)를 나타낸다.", True,
       "데이터를 구간으로 나눠 각 구간의 빈도를 막대 높이로 표현하는 것이 히스토그램이다.", "p.5"),
    ox("q9-03", 9, "px.bar()는 시간에 따른 변화를 나타내는 꺾은선그래프를 그리는 함수이다.", False,
       "px.bar()는 막대그래프(범주별 크기 비교)다. 꺾은선그래프는 px.line()이다.", "p.16, 21"),
    ox("q9-04", 9, "Seaborn은 Matplotlib을 바탕으로 만든 고급 시각화 라이브러리로, 코드가 간결하고 기본 테마가 예쁘다.", True,
       "Seaborn은 Matplotlib 기반이고 코드가 간결하며 통계적 시각화에 강하다. 대신 Matplotlib보다 자유도가 낮다.", "p.1"),
    mc("q9-05", 9, "Plotly Express를 px라는 이름으로 불러오는 올바른 코드는?",
       ["import plotly.express as px", "import express.plotly as px", "import plotly.px as express", "from px import plotly"], 0,
       "모듈 경로는 plotly.express이고 as px로 별칭을 붙인다.", "p.4"),
    mc("q9-06", 9, "분석 목적과 그래프 종류가 올바르게 짝지어진 것은?",
       ["개봉연도별 평균 평점의 변화 추세 - 꺾은선그래프",
        "영화 평점의 분포 확인 - 꺾은선그래프",
        "시간에 따른 평균 주문금액 변화 - 히스토그램",
        "음식종류별 주문 횟수 비교 - 꺾은선그래프"], 0,
       "분포는 히스토그램, 시간·순서에 따른 변화는 꺾은선, 범주별 크기 비교는 막대그래프가 알맞다.", "p.5, 16, 21"),
    mc("q9-07", 9, "영화 투표수(No_of_Votes)의 분포를 히스토그램으로 나타내는 올바른 코드는?",
       ["px.histogram(df, x='No_of_Votes')", "px.line(df, x='No_of_Votes')", "px.bar(df, x='No_of_Votes')", "px.show(df, x='No_of_Votes')"], 0,
       "히스토그램 함수는 px.histogram()이다. px.show라는 함수는 없고 그래프를 화면에 그리는 것은 fig.show()다.", "p.6"),
    mc("q9-08", 9, "다음 코드에서 nbins=25의 의미는?",
       ["히스토그램의 구간 개수를 약 25개로 설정한다.", "영화 25편만 그래프에 표시한다.", "평점이 25점 이상인 영화만 선택한다.", "그래프의 가로 길이를 25로 설정한다."], 0,
       "nbins는 구간(bin)의 개수다. 값이 클수록 구간이 잘게 나뉜다. 구간 너비는 (최댓값 − 최솟값) ÷ nbins다.", "p.6, 8",
       code="fig = px.histogram(df, x='IMDB_Rating', nbins=25)", reported="nbins"),
    mc("q9-09", 9, "영화 평점 히스토그램에서 9.0점 이상 구간의 막대가 매우 낮다. 올바른 해석은?",
       ["9.0점 이상의 높은 평점을 받은 영화는 상대적으로 적다.", "9.0점 이상의 영화는 하나도 없다.", "모든 영화의 평균 평점이 9.0점이다.", "평점이 낮은 영화가 가장 적다."], 0,
       "막대가 낮다는 것은 그 구간의 영화 수가 적다는 뜻이다. 없는 것은 아니다(막대가 0이 아니다).", "p.7"),
    mc("q9-10", 9, "Plotly 도구 모음에서 그래프를 처음 상태로 되돌리는 기능은?",
       ["Reset Axes (집 모양)", "Autoscale (화살표 회전)", "Pan (손바닥)", "Zoom (돋보기)"], 0,
       "Reset Axes가 초기 상태로 복원한다. Autoscale은 데이터 범위에 맞게 축을 자동 조정, Pan은 이동, Zoom은 확대다.", "p.11"),
    mc("q9-11", 9, "다음 코드의 실행 결과는?",
       ["20000.0", "15000.0", "60000", "18000.0"], 0,
       "2026-02 묶음은 15000, 30000, 15000이고 평균은 20000.0이다. 15000.0은 1월 평균, 18000.0은 전체 평균이다.", "p.15",
       code="df = pd.DataFrame({\n    '주문년월': ['2026-01', '2026-01', '2026-02', '2026-02', '2026-02'],\n    '주문금액': [10000, 20000, 15000, 30000, 15000]\n})\nmonthly = df.groupby('주문년월')['주문금액'].mean()\nprint(monthly['2026-02'])", expect="20000.0"),
    mc("q9-12", 9, "다음 코드의 실행 결과는?",
       ["3", "2", "5", "60000"], 0,
       "count()는 묶음마다 주문ID의 개수를 센다. 2026-02는 3건이다.", "p.20",
       code="df = pd.DataFrame({\n    '주문ID': [1, 2, 3, 4, 5],\n    '주문년월': ['2026-01', '2026-01', '2026-02', '2026-02', '2026-02']\n})\ntransactions = df.groupby('주문년월')['주문ID'].count()\nprint(transactions['2026-02'])", expect="3"),
    mc("q9-13", 9, "monthly_amount = df.groupby('주문년월')['주문금액'].mean() 에서 monthly_amount.index와 monthly_amount.values는 각각 무엇인가?",
       ["index는 주문년월 값들, values는 월별 평균 주문금액들", "index는 월별 평균 주문금액들, values는 주문년월 값들", "index와 values 모두 주문ID", "index는 0부터 239까지의 행 번호, values는 주문년월"], 0,
       "groupby의 기준 열(주문년월)이 결과의 index가 되고, 계산된 평균이 values가 된다. 그래서 x=index, y=values로 그래프를 그린다.", "p.15"),
    mc("q9-14", 9, "막대그래프의 X축 이름을 '월', Y축 이름을 '횟수'로 바꾸기 위해 빈칸에 들어갈 코드는?",
       ["labels={'x': '월', 'y': '횟수'}", "labels=['월', '횟수']", "title={'x': '월', 'y': '횟수'}", "xlabel='월', ylabel='횟수'"], 0,
       "px.bar()의 labels는 딕셔너리다. xlabel, ylabel은 Matplotlib 방식이라 Plotly에서는 쓰지 않는다.", "p.22",
       code="fig = px.bar(\n    transactions,\n    x=transactions.index,\n    y=transactions.values,\n    _____\n)", reported="bar"),
    # ----- 나왔다고 함: nbins·구간 너비, 막대 x·y
    mc("q9-16", 9, "영화 평점의 최솟값이 7.0, 최댓값이 9.0이다. 다음 코드로 히스토그램을 그리면 구간 하나의 너비는?",
       ["0.1", "0.2", "2.0", "20"], 0,
       "구간 너비 = (최댓값 − 최솟값) ÷ nbins = (9.0 − 7.0) ÷ 20 = 0.1이다. 2.0은 나누기 전의 범위, 20은 구간 개수다.", "p.8",
       code="fig = px.histogram(df, x='IMDB_Rating', nbins=20)", reported="nbins"),
    mc("q9-17", 9, "영화 평점 히스토그램의 구간 개수를 20개로 바꾸려고 한다. 빈칸에 들어갈 코드는?",
       ["nbins=20,", "bins=20,", "nbin=20,", "size=20,"], 0,
       "구간 개수는 nbins 매개변수로 정한다. 이름이 정확히 nbins다(bins, nbin이 아니다).", "p.8",
       code="fig = px.histogram(\n    df,\n    x='IMDB_Rating',\n    _____\n    title='영화 평점 분포'\n)\nfig.show()", reported="nbins"),
    ox("q9-18", 9, "히스토그램의 nbins 값을 크게 하면 구간 너비가 넓어져 분포가 더 뭉뚱그려 보인다.", False,
       "nbins가 크면 같은 범위를 더 많이 나누므로 구간 너비가 좁아지고 더 세밀한 분포가 보인다.", "p.8", reported="nbins"),
    mc("q9-19", 9, "월별 주문 횟수 막대그래프에서 X축은 주문년월, Y축은 주문 횟수가 되도록 빈칸에 들어갈 코드는?",
       ["x=transactions.index, y=transactions.values",
        "x=transactions.values, y=transactions.index",
        "x=transactions.index(), y=transactions.values()",
        "x=transactions, y=transactions.count()"], 0,
       "groupby 결과의 index는 묶은 기준(주문년월), values는 센 값(주문 횟수)이다. index와 values는 속성이라 괄호를 붙이지 않는다. 둘을 바꾸면 축이 뒤바뀐다.", "p.21–22",
       code="transactions = df.groupby('주문년월')['주문ID'].count()\nfig = px.bar(\n    transactions,\n    _____,\n    title='월별 배달음식 주문 횟수'\n)", reported="bar"),
    mc("q9-15", 9, "월별 평균 주문금액(1월 21000, 2월 17000, 3월 24000, 4월 19000)을 꺾은선그래프로 그렸을 때 올바른 해석은?",
       ["3월이 가장 높고 2월이 가장 낮다.", "1월부터 4월까지 매월 증가한다.", "2월이 가장 높다.", "4월이 1월보다 높다."], 0,
       "값을 비교하면 3월 24000이 최대, 2월 17000이 최소다. 4월(19000)은 1월(21000)보다 낮고 매월 증가하지도 않는다.", "p.18"),
]
