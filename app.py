import streamlit as st

st.set_page_config(page_title="AI 마을 시뮬레이터", layout="wide")

st.title("🌌 AI 마을 시뮬레이터")
st.markdown("각 캐릭터는 인간처럼 사고하며, 실시간으로 행동하고 대화합니다.")
st.markdown("---")

st.header("📍 마을 지도")
st.write("🏠 헬레나의 집 | 🧙 장로의 집 | 🎓 파우스트 노트 | 🍞 식당 | 🎨 제시카 공방 | 🛠 마이클 공터")

st.header("🧠 캐릭터 상태")
st.write("👤 파우스트: '그 판단에는 의미가 없습니다. 하지만 기록하죠.'")
st.write("👤 미에르: '아직은 잘 모르겠어요...'")
st.write("👤 마이클: '규칙? 재밌어야 따르죠!'")
st.write("👤 헬레나: '이건 그냥 생각이에요. 아무 의미는 없어요.'")
st.write("👤 제시카: '응~ 뭐든 괜찮아.'")
st.write("👤 장로: '이 마을의 룰은 질서에서 나온다.'")

st.header("📓 파우스트의 노트")
st.code("""
- 미에르: 불확실한 감정 표현 확인.
- 마이클: 일관된 낙천성 유지 중.
- 헬레나: 창의성 점진적 상승.
""", language='markdown')
