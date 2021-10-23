import playsound
import os
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup
import time
from googlesearch import search
import subprocess
import datetime
import random
from pynput.keyboard import Key,Controller
import psutil
import wikipedia
from deep_translator import GoogleTranslator

keyboard = Controller()

def speak_t(text):
    tts=gTTS(text=text,lang="tr")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 160)
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said = ""

        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()
def get_audio_eng():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said = ""

        try:
            said=r.recognize_google(audio,language="en-US")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()


def get_audio_withoutwriting():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("")
    return said.lower()
def get_audio_withoutwriting_eng():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio,language='en-US')
        except Exception as e:
            print("")
    return said.lower()




def alarm_tanıma(t):
    süre=""
    for i in t:
        for x in range(0, 10):
            try:
                if int(i) ==x:
                    süre += i
            except:
                continue
    if t.count("dakika")>0:
        if t.count("buçuk")>0:
            süree=int(süre)*60+30
        else:
            süree=int(süre)*60
    if t.count("saniye")>0:
        süree=int(süre)

    time.sleep(int(süree))
    playsound.playsound("Crystal.mp3")
    speak("Time is up sir")


def film_bul(irating):
    url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    response = requests.get(url)
    içerik = response.content
    soup = BeautifulSoup(içerik,"html.parser")
    başlıklar = soup.find_all("td",{"class","titleColumn"})
    ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})

    for başlık,rating in zip(başlıklar,ratingler):
        başlık = başlık.text
        başlık = başlık.strip()
        başlık = başlık.replace("\n","")

        rating = rating.text
        rating  = rating.strip()
        rating = rating.replace("\n","")
        if float(rating)>float(irating):
            print("Filmin İsmi {} Filmin Ratingi {}".format(başlık,rating))

def film_seç():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    response = requests.get(url)
    içerik = response.content
    soup = BeautifulSoup(içerik, "html.parser")
    başlıklar = soup.find_all("td", {"class", "titleColumn"})
    ratingler = soup.find_all("td", {"class", "ratingColumn imdbRating"})

    speak("Tell me the number of the film?")
    x=get_audio()

    if x=="bir":
        x=1
    isim =""
    sıra = 1
    for başlık, rating in zip(başlıklar, ratingler):
        if int(x) == sıra:
            başlık = başlık.text
            başlık = başlık.strip()
            başlık = başlık.replace("\n", "")

            rating = rating.text
            rating = rating.strip()
            rating = rating.replace("\n", "")
            isim = başlık
            break
        else:
            sıra += 1
            continue

    for i in range(0, 10):
        isim = isim.replace(str(i), "")
    isim = isim.replace(".", "")
    isim = isim.replace("()", "")
    isim = isim.strip()

    searchengine = "https://www.google.com/search?q=" + (isim)+" izle"
    webbrowser.open(searchengine)
    return False

def bekleme(answer):
    while True:
        if answer=="hayır":
            time.sleep(15)
        elif answer=="evet":
            break

def googlesearch(answer):

    searchengine = "https://www.google.com/search?q=" + (answer)
    webbrowser.open(searchengine)

def not_alma(text):
    FILE_NAME="Memory/notlar.txt"
    with open(FILE_NAME,"a",encoding="utf-8") as file:
        file.write(text)
        file.write("\n")
    subprocess.Popen(["notepad.exe",FILE_NAME])
    speak("Done")
def notları_oku():
    FILE_NAME = "Memory/notlar.txt"
    words1 = ""
    with open(FILE_NAME, "r+", encoding="utf-8") as file:
        for i in file.readlines():
            print(i)
            speak_t(i)
def notları_göster():
    FILE_NAME = "Memory/notlar.txt"
    subprocess.Popen(["notepad.exe",FILE_NAME])
def notları_yazdır():
    FILE_NAME = "Memory/notlar.txt"
    words2 = ""
    with open(FILE_NAME, "r+", encoding="utf-8") as file:
        for i in file:
            words2 += i
            print(words2)
def notları_temizle():
    FILE_NAME = "Memory/notlar.txt"
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write("")

def liste_aç():
    döngü=True
    while döngü:
        speak("How do you want to name it?")
        FILE = get_audio()
        if FILE!="":
            FILE_NAME = f"{FILE}.txt"
            döngü=False
    open(FILE_NAME, "w", encoding="utf-8")
    speak("What do you want to write?")
    CONTENT=get_audio()
    with open(FILE_NAME, "r+", encoding="utf-8") as file:
            file.write(CONTENT)
    speak("Noted...")
def listeye_yaz():
    speak("Which list do you want to edit?")
    LIST = get_audio()
    LIST_NAME= f"{LIST}.txt"
    speak("What do you want to write?")
    CONTENT = get_audio()
    try:
        with open(LIST_NAME, "r+", encoding="utf-8") as file:
                file.write(CONTENT)
    except:
        speak("There is a mistake")
def ses_kıs(ses):
    for i in range(ses):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
def ses_aç(ses):
    for i in range(ses):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
def hava_durumu():
    url = "https://www.google.com/search?q=hava+durumu+samsun+k%C3%B6rfez&oq=hava&aqs=chrome.0.69i59j69i57j69i59j0i131i433l2j0i433j0i131i433l2.12187j1j7&sourceid=chrome&ie=UTF-8"
    response = requests.get(url)
    içerik = response.content
    soup = BeautifulSoup(içerik, "html.parser")
    derece = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).text
    hava = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).find_next().find_next().find_next().text
    speak(f"Outside is {derece}")
    speak(GoogleTranslator(source='auto', target='en').translate(hava))

def translate():
    speak("Which language you want to translate?")
    while True:
        try:
            answer5=get_audio()
            if answer5.count("english")>0:
                speak("English to Turkish. What is the text?")
                while True:
                    to_translate=get_audio_eng()
                    if to_translate.count("that is it")>0 or to_translate.count("bu kadar")>0:
                        speak("As you wish...")
                        break
                    else:
                        print(GoogleTranslator(source='auto', target='tr').translate(to_translate))
                        speak_t(GoogleTranslator(source='auto', target='tr').translate(to_translate))
                break
            if answer5.count("türkçe")>0:
                speak("Turkish to English. What is the text?")
                while True:
                    to_translate=get_audio()
                    if to_translate.count("that is it")>0 or to_translate.count("bu kadar")>0:
                        speak("As you wish...")
                        break
                    else:
                        print(GoogleTranslator(source='auto', target='en').translate(to_translate))
                        speak(GoogleTranslator(source='auto', target='en').translate(to_translate))

                break
        except:
            speak("There is a mistake")

