from gtts import gTTS
import random
import os
#from pygame import mixer

def speak(rand,n,mixer):
    text = random.choice(rand)
    tts = gTTS(text, lang='en')
    dirname = os.path.dirname(__file__)
    #change this if you are using windows
    path=r"C:/Users/pratiksha shetty/Desktop/J.A.R.V.I.S-master/audio/"+text+str(n)+'.mp3'
    filename = os.path.join(dirname,path) 
    #print(filename)                
    tts.save(filename)

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

def speek(rand,n,mixer):
    text = random.choice(rand)
    tts = gTTS(text, lang='en')
    dirname = os.path.dirname(__file__)
    #change this if you are using windows
    path=r"C:/Users/pratiksha shetty/Desktop/J.A.R.V.I.S-master/audio/"+"jarvis"+str(n)+'.mp3'
    filename = os.path.join(dirname,path) 
    #print(filename)                
    tts.save(filename)

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

def wifi():
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False

# def play(filename,mixer):
#     mixer.init()
#     mixer.music.load(filename)
#     mixer.music.play()
#     return True
