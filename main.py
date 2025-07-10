import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 여행지 추천기", page_icon="🌍")

# 제목
st.title("✈️ 나에게 꼭 맞는 여행지는 어디일까?")
st.subheader("MBTI를 선택하면 여행지가 짠! 하고 나타납니다. 🎁")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 사용자 입력 받기
selected_mbti = st.selectbox("📌 당신의 MBTI를 선택하세요!", mbti_types)

# 여행지 추천 데이터
mbti_travel = {
    "ISTJ": [
        ("교토 🇯🇵", "전통과 질서가 살아있는 도시. 역사적인 절과 정원이 ISTJ의 차분한 성향과 어울려요."),
        ("하이델베르크 🇩🇪", "학문과 규범의 도시. 고요한 환경에서 사색하며 여행을 즐기기 좋아요."),
        ("세도나 🇺🇸", "명상과 자연이 조화를 이루는 곳. 혼자만의 시간을 보내기 좋아요.")
    ],
    "ENFP": [
        ("바르셀로나 🇪🇸", "창의적이고 생동감 넘치는 도시. 가우디 건축물과 활기찬 거리 공연이 ENFP의 에너지와 딱 맞아요!"),
        ("치앙마이 🇹🇭", "열정적이고 사람들과 교류하기 좋은 환경. 다양한 액티비티도 가득!"),
        ("리우데자네이루 🇧🇷", "흥과 자유를 동시에! 리듬에 몸을 맡기고 여행을 즐기기 좋은 도시예요.")
    ],
    "INFJ": [
        ("레이캬비크 🇮🇸", "자연 속에서 깊이 있는 성찰이 가능한 곳. 오로라와 온천은 감성을 자극해요."),
        ("프라하 🇨🇿", "예술과 철학이 녹아든 도시. 조용한 골목에서 자신만의 시간을 보내기 좋아요."),
        ("시애틀 🇺🇸", "책과 커피, 비 오는 날씨. INFJ에게는 완벽한 감성 도시!")
    ],
    "ESTP": [
        ("두바이 🇦🇪", "화려함과 액티비티의 천국! 빠른 자극을 좋아하는 ESTP에게 딱."),
        ("시드니 🇦🇺", "서핑, 클럽, 자유! 에너지 넘치는 도시 생활이 가능합니다."),
        ("라스베이거스 🇺🇸", "즉흥적인 즐거움! 하루가 모자란 밤의 도시.")
    ],
    # 나머지 MBTI는 샘플로 동일한 구조로 추가하면 돼!
}

# 추천 결과 표시
if selected_mbti in mbti_travel:
    st.markdown("### 🎯 추천 여행지")
    for place, reason in mbti_travel[selected_mbti]:
        st.markdown(f"#### 📍 {place}")
        st.write(f"👉 {reason}")
    st.balloons()  # 풍선 효과 🎈
else:
    st.warning("아직 이 MBTI에 대한 추천 여행지가 등록되지 않았어요. 곧 추가됩니다! 🚧")
