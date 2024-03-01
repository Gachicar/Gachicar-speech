import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[사용자]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print("요청 실패 : {0}".format(e))


def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 가치카입니다.'
    elif '학교로 가' in input_text: 
        answer_text = '네 알겠습니다.'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
    elif '종료' in input_text:
        answer_text = '가치카를 이용해주셔서 감사합니다.'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    speak(answer_text)

# 소리내어 읽기 (TTS)
def speak(text):
    print('[가치카]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)

while True:
    time.sleep(0.1)