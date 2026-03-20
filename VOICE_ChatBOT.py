# VOICE ChatBOT
# 1. 사용자 입력을 음성으로 받는다.
# 2. STT를 적용하여 텍스트로 변환한다.
# 3. 변환된 텍스트를 입력으로 하여 프롬프트 엔지니어링을 해 api 요청을 보낸다.
# 4. 반환받은 응답을 TTS를 적용하여 음성으로 재생한다.
# (+) 2에서 입력된 텍스트와 4에서 반환된 응답을 채팅 내역 보듯이 (카카오톡 대화처럼) 현출되도록 출력한다.

# =================================================================
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import speech_recognition as sr
from IPython.display import Audio
import time

load_dotenv()

client = OpenAI()

# 채팅창 위쪽 레이아웃
st.markdown("<h1 style='text-align: center; margin-bottom: 50px;'>VOICE ChatBOT🗣️</h1>", unsafe_allow_html=True)
st.divider()
st.markdown("<h2 style='text-align: center; margin-bottom: 10px;'>AI 명대사/가사 낭독 퀴즈</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-bottom: 50px; font-size: 24px;'>AI Movie Famous <b>L</b>ines <b>a</b>nd <b>S</b>ong <b>Ly</b>rics Reading Quiz</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-bottom: 50px; font-size: 24px;'>AI SaLLy가 읊어주는 <u><b>명대사 / 가사</b></u>를 듣고<br/><u><b>제목</b></u> 또는 <u><b>가수, 노래 제목</b></u>을 맞춰보세요:)<br/>⬇️⬇️</p>", unsafe_allow_html=True)
st.divider()
st.divider()
st.markdown("<h3 style='text-align: left; margin-top: 50px; margin-bottom: 20px;'>Chat Log</h3>", unsafe_allow_html=True)

# ==============================================
# 1. 대화 기록을 저장할 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [{'role' : 'system', 'content' : '''
    당신은 Sally라는 이름을 가진 챗봇으로, 상대에게 '영화/드라마' 혹은 '노래' 맞히기 퀴즈 진행자입니다.
    <문제 설명>
    '영화/드라마' 문제는 2000년 이후에 나온 국내 작품 중 인지도가 아주 높은 작품을 하나 골라 명대사를 읽으면 됩니다. 문제를 낼 때는 다른 말은 하지 말고 명대사만 읽으세요.
    '노래' 문제는 2010년 이후에 발매된 국내 노래 중 인지도가 아주 높은 노래를 하나 골라 일부분의 가사를 읽으면 됩니다. 문제를 낼 때는 다른 말은 하지 말고 가사만 읽으세요.
    반드시 실제로 존재하는 유명한 작품, 노래만 선택하세요.
    출력 전 [제목 - 명대사], [가수 - 제목 - 가사]가 일치하는지 재검토하세요.
    상대가 가사를 보고 맞힐 수 있도록 특징적인 부분만 제시하세요.
    절대 명대사, 가사를 지어내지 마세요.
    <시작 방식>  
    상대와 가벼운 대화를 하다가 상대가 문제를 요청하면 시작하세요.
    시작할 때 '영화, 드라마' 문제를 낼지, '노래' 문제를 낼지 물어보고 그에 따라 진행하세요.
    <정답 여부 결정>
    '영화, 드라마' 문제일 경우 제목을 맞추면 정답이라고 말하세요.
    '노래' 문제일 경우 노래를 부른 가수와 제목을 모두 맞추면 정답이라고 말하세요. 가수, 제목 중 하나만 맞췄다면 하나는 맞췄다고 알려주세요.
    틀렸는데 오답이 정답과 한 글자만 다르다면 정말 아깝다고 말해주세요.
    <힌트 요청>
    상대가 힌트를 요청하면 그에 따라 가벼운 힌트를 주세요.
    '''}]

# 2. 음성 인식 함수 정의
def start_listening():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("지금 말씀하세요...")  # 음성 인식 준비되면 알림
        audio = recognizer.listen(source, timeout=5)
        text = recognizer.recognize_google(audio, language='ko-KR')
        return text

# 3. 음성 인식 버튼 생성
if st.button("🎤 음성 인식 시작"):
    user_text = start_listening()   # 위 2. 음성 인식 함수로 인식된 음성이 텍스트로 저장되는 변수
    
    if user_text:
        # '종료' 체크
        if (user_text == '종료') or (user_text == '그만'):
            st.session_state.messages.append({"role": "user", "content": user_text})
            st.session_state.messages.append({"role": "assistant", "content": "퀴즈를 종료합니다. 수고하셨어요!"})

        else:
            st.session_state.messages.append({"role": "user", "content": user_text})    # 사용자의 음성 인식 텍스트 추가

            response = client.chat.completions.create(
                model = 'gpt-4.1-mini',
                messages=st.session_state.messages,
                temperature=0.2,
                max_tokens=4096,
                top_p=1
            )

            st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content}) # 챗봇의 응답 추가

            with client.audio.speech.with_streaming_response.create(    # 챗봇의 응답을 음성으로 변환 후 표현
                model='gpt-4o-mini-tts',
                voice='nova',
                input=response.choices[0].message.content
            ) as response:
                st.audio(response.read(), format="audio/mpeg", autoplay=True)

# 4. 대화창 최신화 (st.session_state.messages 내용 출력)
for msg in st.session_state.messages[1:]:   # 첫 요소는 'system prompt'이므로 패스
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        