import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 취미 추천기", page_icon="🎨")

# 타이틀
st.title("🧠 MBTI별 나에게 꼭 맞는 취미는?")
st.subheader("성격에 딱 맞는 취미를 찾아드립니다! 🎯")

# MBTI 목록
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 사용자 입력 받기
selected_mbti = st.selectbox("📌 MBTI를 선택하세요!", mbti_list)

# MBTI별 취미 추천 사전
mbti_hobbies = {
    "INTJ": {
        "hobbies": ["체스 ♟️", "코딩 💻", "문예창작 ✍️"],
        "highlight": ("문예창작 ✍️", "자신의 사고와 세계관을 깊이 있게 표현할 수 있는 활동으로, INTJ의 내면 세계와 잘 어울립니다.")
    },
    "ENFP": {
        "hobbies": ["춤 배우기 💃", "즉흥 연극 🎭", "배낭여행 🌍"],
        "highlight": ("즉흥 연극 🎭", "ENFP의 에너지와 창의성을 마음껏 발휘할 수 있는 활동입니다! 사람들과의 교감도 강하게 느낄 수 있어요.")
    },
    "ISFJ": {
        "hobbies": ["자수 🧵", "베이킹 🍪", "사진 찍기 📷"],
        "highlight": ("베이킹 🍪", "조용한 집중력과 섬세한 손길이 필요한 활동으로, ISFJ의 세심함이 빛을 발할 수 있어요.")
    },
    "ESTP": {
        "hobbies": ["서핑 🏄‍♂️", "클라이밍 🧗", "스카이다이빙 🪂"],
        "highlight": ("서핑 🏄‍♂️", "즉각적인 반응과 몸으로 부딪히는 활동을 좋아하는 ESTP에게 최고의 선택이에요!")
    },
    "INFP": {
        "hobbies": ["시 쓰기 ✒️", "명상 🧘", "수채화 그리기 🎨"],
        "highlight": ("수채화 그리기 🎨", "자신만의 감성과 내면을 부드럽게 표현할 수 있어 INFP에게 큰 만족감을 줄 수 있어요.")
    },
    # 나머지 MBTI는 필요 시 추가 가능!
}

# 출력
if selected_mbti in mbti_hobbies:
    st.markdown("### 🧩 추천 취미 활동")
    for hobby in mbti_hobbies[selected_mbti]["hobbies"]:
        st.markdown(f"- {hobby}")
    
    highlight, reason = mbti_hobbies[selected_mbti]["highlight"]
    st.markdown("### 🌟 꼭 해보면 좋은 취미 활동")
    st.markdown(f"**{highlight}**")
    st.write(f"👉 {reason}")
    st.balloons()
else:
    st.warning("아직 이 MBTI 유형에 대한 취미 정보가 준비 중입니다. 조금만 기다려주세요! 🙏")
