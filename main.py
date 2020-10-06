import wikipedia
import wolframalpha
from tkinter import *
import speech_recognition as sr

while True:
    # lets create the object of Recognizer class
    r = sr.Recognizer()

    # deciding the source of input, here it is microphone
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)  # this audio variable is holding the audio speak by you
        try:
            print("Recognizing........")
            # lets convert the audio into text
            text = r.recognize_google(audio)
            print("you said..." + text)
            if text == "stop":
                break
            else:
                window = Tk()
                window.geometry("700x600")
                # here i can give answer either with wolframalpha or wikipedia
                # wolframalpha is give answer related to questions like hii, hello, your name etc
                # and wikipedia answer the questions in details like about steve jobs etc
                try:
                    # here answer using wolframalpha
                    # so for doing this i have to use the api of wolframalpha
                    app_id = "my wolframAlpha API id is here"
                    client = wolframalpha.Client(app_id)
                    res = client.query(text)
                    answer = next(res.results).text
                    print('Answer from wolframAlpha: ')
                    print(answer)
                    label = Label(window,
                                  justify=LEFT,
                                  wraplength=650,
                                  compound=CENTER, padx=10,
                                  text=answer,
                                  font='times 15 bold')
                    label.pack()
                    window.after(5000, lambda: window.destroy())
                    mainloop()
                except Exception as e:
                    print("No results from wolframalpha. trying wikipedia.........")
                    answer = wikipedia.summary(text)
                    print('Answer from wikipedia: ')
                    print(answer)
                    label1 = Label(window,
                                   justify=LEFT,
                                   wraplength=650,
                                   compound=CENTER, padx=10,
                                   text=answer,
                                   font='times 15 bold')
                    label1.pack()
                    window.after(5000, lambda: window.destroy())
                    mainloop()
        except Exception as e:
            print(e)
            answer = "Sorry we cant hear you"
            print(answer)
