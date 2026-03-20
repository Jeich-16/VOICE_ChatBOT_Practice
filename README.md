# VOICE_ChatBOT_Practice

*"TTS와 STT, Prompt Engineering을 활용한 Chatbot 만들기"*<br/>
## AI 명대사/가사 낭독 퀴즈
#### AI Movie Famous Lines and Song Lyrics Reading Quiz
---

<br/><br/>

## 📋 개요
![123](https://github.com/user-attachments/assets/d8f8698d-5b08-4c04-a92c-ab41805fa22b)
[출처](https://blog.naver.com/PostView.nhn?blogId=muldorn&logNo=221853321797&parentCategoryNo=&categoryNo=222&viewDate=&isShowPopularPosts=true&from=search)
> tvN 예능 프로그램 <놀라운 토요일 - 도레미 마켓><br/><br/>
> 본 서비스는 AI가 낭독하는 영화/드라마 명대사나 노래 가사를 듣고, 사용자가 음성으로 정답을 맞히는 양방향 소통형 퀴즈입니다.<br/>
> 단순 텍스트 기반 퀴즈를 넘어 말하기(STT)와 듣기(TTS), 대화하기(with ChatBOT)가 결합된 다양한 경험을 제공합니다.

<br/><br/>

## 적용 기술
|   기술   | 내용            | 모델 |
|:--------:|:-----------------:|:-----------------:|
| STT | 사용자의 음성을 실시간으로 인식하여 텍스트로 변환 | speech_recognition |
| TTS | AI 모델의 답변 텍스트를 자연스러운 음성으로 변환 | gpt-4o-mini-tts |
| Prompt Engineering | 낭독 퀴즈를 원활히 진행할 수 있도록 문맥 유지 | gpt-4.1-mini |
| 웹 인터페이스 | Chat Log UI 구현 실시간 반영 | streamlit |

<br/><br/>

## Workflow
> 퀴즈 분야 확인 후 생성<br/>
- 영화/드라마 퀴즈를 할지, 노래 퀴즈를 할지 결정<br/>
> 문제 낭독<br/>
- AI 보이스로 다른 말 없이 문제만 낭독
> 정답 입력 또는 힌트 요청<br/>
- 버튼 클릭 후 사용자의 음성으로 정답 입력 또는 힌트 요청
> 결과 피드백<br/>
- 정답이면 추가 문제 제안, 오답이면 새 힌트 제안

<br/><br/>

---

## 진행 결과
<img width="450" height="auto" alt="01" src="https://github.com/user-attachments/assets/d2da10a0-e661-4d7c-87be-d4dbc658693d" />  
<img width="450" height="auto" alt="02" src="https://github.com/user-attachments/assets/8c3425b9-798b-437f-8877-1c9f2ebfd834" /><br/><br/>
<img width="450" height="auto" alt="03" src="https://github.com/user-attachments/assets/3b1d39f6-3f5a-48e9-a373-17b12e88f664" />  
<img width="450" height="auto" alt="04" src="https://github.com/user-attachments/assets/60a94a53-bdb6-4387-a4ce-c986690025ed" /><br/><br/>

<br/><br/>

## 한계점
