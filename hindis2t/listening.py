
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


def recog():
    with mic as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # with open("./audio/testing.wav", "wb") as f:
    #     f.write(audio.get_wav_data())
    try:
        text = r.recognize_google(audio, language="hi-IN")
        # text = r.recognize_google(audio)
        with open("test.txt", "a") as fil:
            fil.write(text)
            fil.write("\n--\n")

        return(text)
    except:
        return("sorry")


def aud():
    with mic as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    with open("./audio/testing.wav", "wb") as f:
        f.write(audio.get_wav_data())

# try:
#     print(r.recognize_google(audio))
# except sr.RequestError:
#     print("sorry net not available")
# except sr.UnknownValueError:
#     print("sorry did not understand")
