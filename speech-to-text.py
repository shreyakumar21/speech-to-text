import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak what scene you would wish to see: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}', format(text))

        with open("input.txt","a") as f:
            f.write(text)
        print(text)

    except:
        print('Sorry, we could not recognize your voice..')