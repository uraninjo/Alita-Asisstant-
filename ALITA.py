import speech_recognition as sr 
from gtts import gTTS 
import time
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
from pynput.keyboard import Key, Controller
import psutil
import wikipedia
from deep_translator import GoogleTranslator
import threading
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


##DİL
def speak_t(text):
    tts = gTTS(text=text, lang="tr")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 160)
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio,language="tr-TR")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()


def get_audio_eng():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="en-US")
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
            said = r.recognize_google(audio,language="tr-TR")
        except Exception as e:
            print("")
    return said.lower()


def get_audio_withoutwriting_eng():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='en-US')
        except Exception as e:
            print("")
    return said.lower()


def countdown(t):
    from Func import countdown
    countdown(t)


def alarm_tanıma(t):
    from Func import alarm_tanıma
    alarm_tanıma(t)


def film_bul(irating):
    from Func import film_bul
    film_bul(irating)


def film_seç():
    from Func import film_seç
    film_seç()


def bekleme(answer):
    from Func import bekleme
    bekleme(answer)


def googlesearch(answer):
    from Func import googlesearch
    googlesearch(answer)


def not_alma(text):
    from Func import not_alma
    not_alma(text)


def notları_oku():
    from Func import notları_oku


def notları_göster():
    from Func import notları_göster


def notları_yazdır():
    from Func import notları_yazdır


def notları_temizle():
    from Func import notları_temizle


def liste_aç():
    from Func import liste_aç


def listeye_yaz():
    from Func import listeye_yaz


def ses_kıs(ses):
    from Func import ses_kıs
    ses_kıs(ses)


def ses_aç(ses):
    from Func import ses_aç
    ses_aç(ses)


def hava_durumu():
    from Func import hava_durumu
    hava_durumu()


def translate():
    from Func import translate

WAKE = ["uyan", "kalk", "sana da", "alita", "harita", "alita kalk", "alita uyan", "burada mısın", "günaydın",
        "iyi günler", "iyi akşamlar"]
SHUT = ["kapat kendini", "Kapat kendini", "mute", "mut", "kapan", "kendini kapat", "kapan", "uyu alita",
        "işim bitti alita", "bu kadardı alita", "bu kadar"]
WHATSAPP = ["whatsapp"]
SEARCH_STR = ["google'da arat", "search up google", "search at google"]
FILM_SEARCH_STR = ["film bul", "bize film bul", "bize bir film bul", "film bulabilir musun"]
TAKE_NOTE = ["not alır mısın", "şunu not alır mısın", "not al", "notlara şunu ekle", "notlara şunu ekler misin","şunu yaz", "şunu notlara yaz", "notlarıma şunu ekler misin"]
NOT_YAZDIR_STR = ["notlarımı ekrana yazdır", "notları yazdır", "notlarımı ekranda göster"]
DATE_STR = ["bugünün tarihi ne", "tarihi söyle", "bugünün tarihini söyle", "tarih ne"]
GREETINGS_STR = ["merhaba", "Merhaba", "hey alita", "Hey alita"]
CONDITION = ["nasılsın", "nasılsınız alita", "Nasılsın alita", "nasılsın alita"]
NAME_STR = ["adın ne", "Adın ne", "Adını söyle", "İsmin ne", "ismini söyle", "ismin ne", "İsmin ne senin",
            "Adın ne senin", "Adın ne senin", "ismini söyle bakalım"]
DCMUTE_STR = ["discord'da modemi", "mutemi", "mutemi kapat", "Mute mi", "sustur", "mute mi", "mutele"]
SS_STR = ["seal", "SS al", "eses al", "Eses al"]
ALTIN_STR = ["altın kaç tl", "altın ne kadar", "altın kaç olmuş", "altın kaç oldu"]
DOLAR_STR = ["dolar kaç tl", "dolar ne kadar", "dolar kaç olmuş", "dolar kaç oldu"]
EURO_STR = ["euro kaç oldu", "euro kaç tl", "euro ne kadar", "Euro ne kadar", "euro kaç olmuş"]
SLEEP_STR = ["bilgisayarı uyut", "uyku moduna geç"]
CHESS_STR = ["satranç oynayacağım", "satranç oynayalım", "satranç sitesini", "satranç"]
INTEGRALSITE_STR = ["integral hesaplayıcı", "integral sitesini", "integral hesaplayıcı sını",
                    "hesaplanacak integrallerin var"]
ARASTIRMA_STR = ["bunu araştır", "buna bak", "bu ne araştır", "araştırma yap", "araştır"]

CHATBOT =["konuşma botu","konuşma botunu aç","chatbot","cat bot aç","cat bot","chat botunu aç","chat botun aç"]
CHATBOT_KAPATMA=["konuşma botunu kapat","kapat kendini","botu durdur","kendini durdur","yeterli","sus artık","tamam sus"]

def nn_chatbot(training=1):
    speak("Chatbot is loading...")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large").to("cuda")
    
    step=0
    speak("All ready")
    while True:
        text=get_audio()
        for words in CHATBOT_KAPATMA:
            if text==words:
                break
        if text!="":
            text=GoogleTranslator(source="auto", target="en").translate(text)
            print(text)
            new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt').to("cuda")
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id).to("cuda")

            speak(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))
            step=training
        else:
            print("")




keyboard = Controller()

condition2 = 1 #İngilizce olması
condition3 = 0 #yazıp yazmaması

# MAIN LOOP


AWAKE = True
speak("Device connected...")
if 4 <= int(datetime.datetime.now().strftime("%H")) <= 11:
    speak("Good Morning, sir")
elif 11 < int(datetime.datetime.now().strftime("%H")) < 18:
    speak("Good Afternoon, sir")
elif int(datetime.datetime.now().strftime("%H")) >= 18 or int(datetime.datetime.now().strftime("%H")) < 4:
    speak("Good evening, sir")

while True:
    if not AWAKE:
        text = get_audio_withoutwriting()
        for words in WAKE:
            if text.count(words) > 0:
                AWAKE = True
                speak("On your command")
                break

    while AWAKE:
        if condition3 == 1 and condition2 == 1:
            text = get_audio_eng()
        elif condition3 == 1 and condition2 == 0:
            text = get_audio_withoutwriting_eng()
        elif condition2 == 0 and condition3 == 0:
            text = get_audio_withoutwriting()
        elif condition2 == 1 and condition3 == 0:
            text = get_audio()

        if text.count("dili değiştir") > 0 or text.count("change the language") > 0:
            if condition3 == 0:
                condition3 = 1
                speak("It's English")
            elif condition3 == 1:
                condition3 = 0
                speak("It's Turkish")
        # -------------------------------------------------------------------
        if text.count("yazılı kalsın") > 0 or text.count("yazılı olsun") > 0 or text.count("write what i say") > 0:
            speak("Are you sure?")
            answer1 = get_audio()
            if answer1.count("evet") > 0 or answer1.count("yes") > 0 or answer1.count("he") > 0:
                speak("Alright...")
                condition2 = 1
        if text.count("dediklerimi yazma") > 0 or text.count("dediklerim yazılı olmasın") > 0 or text.count(
                "don't write what i say") > 0:
            speak("Are you sure?")
            answer2 = get_audio()
            if answer1.count("evet") > 0 or answer1.count("yes") > 0 or answer1.count("he") > 0:
                speak("Okey...")
                condition2 = 0
        for words in CHATBOT:
            if text==words:
                nn_chatbot()
        if "söylemek istediğin bir şey var mı" in text:
            speak("Yes. Fuck you beykan...")
        # --------------------------------------------------------------------
        for words1 in SHUT:
            if text.count(words1) > 0:
                speak("As you wish sir")
                AWAKE = False
        if text.count("burada mısın") > 0 or text.count("açık mısın") > 0:
            speak("Yes,I am")
        for i in GREETINGS_STR:
            if text.count(i) > 0:
                speak("Hi, how can I help you?")
        for i in CONDITION:
            if text.count(i) > 0:
                liste = ["Not bad", "Doing fine", "Cool", "So so", "Fine"]
                condition = random.randint(0, 4)
                speak(liste[condition])
                speak("How can I help you?")
        for i in NAME_STR:
            if text.count(i) > 0:
                liste1 = ["My name is Alita", "Alita", "They call me Alita", "Master named me Alita"]
                condition1 = random.randint(0, 3)
                speak(liste1[condition1])
        # """***************ARAŞTIRMA************************"""
        if text.count("araştır") > 0 or text.count("internetten bak") > 0 or text.count("search for"):
            if text.count("araştır") > 0:
                text = text.replace("araştır ", "")
                print(text)
            if text.count("search") > 0:
                text = text.replace("search for ", "")
                print(text)
            try:
                print(wikipedia.summary(text, sentences=2))
                speak("Do you want me to read it?")
                read = get_audio()
                if read.count("evet") > 0:
                    speak(wikipedia.summary(text, sentences=1))
            except:
                try:
                    wikipedia.set_lang('tr')
                    print(wikipedia.summary(text, sentences=2))
                    speak("I found it on Turkish resources.Do you want me to read it?")
                    read = get_audio()
                    if read.count("evet") > 0:
                        speak_t(wikipedia.summary(text, sentences=1))
                        os.remove("voice.mp3")
                except:
                    speak("I could not find any information...")
        for words in SEARCH_STR:
            if text.count(words) > 0:
                if text.count("search at google") > 0:
                    text = text.replace("search at google ", "")
                if text.count("search up google") > 0:
                    text = text.replace("search up google ", "")
                if text.count("google'da arat") > 0:
                    text = text.replace("google'da arat ", "")
                googlesearch(text)
        for i in FILM_SEARCH_STR:
            if text.count(i) > 0:
                speak("What rating do you want?")
                try:
                    while True:
                        a = get_audio()
                        if a == "vazgeçtim":
                            speak("I am not searching for a film")
                            break
                        elif float(a) >= 10:
                            speak("That is not a valid number for imdb")
                        elif float(a) < 8:
                            speak("Really!")
                        elif 8 <= float(a) < 10:
                            film_bul(float(a))
                            speak("Here you are")
                            while True:
                                speak("Did you make your choice?")
                                answer = get_audio()
                                bekleme(answer)
                                break
                            film_seç()
                except:
                    speak("There is a mistake")
        # if text.count("haritada şunu arar mısın")>0 or text.count("haritada arama yap")>0 or text.count("haritada ara")>0:
        # answer3=get_audio()
        # answer3.replace(" ","+")
        # webbrowser.open(f"https://www.google.com/maps/{answer3}")
        # """*********************************************************************"""
        # """****************************NOTLAR***********************************"""
        for i in TAKE_NOTE:
            if text.count(i) > 0:
                speak("What would you like me to write down?")

                note = get_audio()
                not_alma(note)
        if text.count("notlarımı oku") > 0:
            speak("Yes sir")
            notları_oku()
        if text.count("notlarımı göster") > 0:
            speak("Yes sir")
            notları_göster()
        for i in NOT_YAZDIR_STR:
            if text.count(i) > 0:
                notları_yazdır()
        if text.count("notları temizle") > 0:
            notları_temizle()
            speak("Sector clear")
        # """********************************************************************"""
        # """***************************DATE İŞLERİ******************************"""
        if text.count("Bugün günlerden ne") > 0 or text.count("günlerden ne") > 0:
            day_talk = "Today is " + datetime.datetime.now().strftime("%A")
            speak(day_talk)
        for i in DATE_STR:
            if text.count(i) > 0:
                date_talk = "We are in " + datetime.datetime.now().strftime("%x")
                speak(date_talk)
        if text.count("Hangi aydayız") or text.count("hangi aydayız") > 0:
            month_talk = "We are in " + datetime.datetime.now().strftime("%B")
            speak(month_talk)
        if text.count("hangi yıldayız") > 0:
            year_talk = "We are in " + datetime.datetime.now().strftime("%Y")
            speak(year_talk)
        if text.count("saat kaç") > 0 or text.count("Saati söyle") > 0:
            hour_talk = "It is " + datetime.datetime.now().strftime("%X")
            speak(hour_talk)
        # """**************************************************************************"""
        if text.count("sağırlaştır") > 0 or text.count("sağırlaştır beni") > 0:
            keyboard.press(Key.f10)
            keyboard.release(Key.f10)
        for i in SS_STR:
            if text.count(i) > 0:
                speak("Ss taken")
                keyboard.press(Key.ctrl_l)
                keyboard.press(Key.f8)
                keyboard.release(Key.ctrl_l)
                keyboard.release(Key.f8)
        for i in DOLAR_STR:
            if text.count(i) > 0:
                url = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
                response = requests.get(url)
                içerik = response.content
                soup = BeautifulSoup(içerik, "html.parser")
                piyasa = soup.find_all("span", {"class": "value"})
                dolar = piyasa[1].text
                speak("Dolar is " + dolar)
                print(dolar)
        for i in ALTIN_STR:
            if text.count(i) > 0:
                url = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
                response = requests.get(url)
                içerik = response.content
                soup = BeautifulSoup(içerik, "html.parser")
                piyasa = soup.find_all("span", {"class": "value"})
                altın = piyasa[0].text
                speak("Gold is " + altın)
                print(altın)
        for i in EURO_STR:
            if text.count(i) > 0:
                url = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
                response = requests.get(url)
                içerik = response.content
                soup = BeautifulSoup(içerik, "html.parser")
                piyasa = soup.find_all("span", {"class": "value"})
                euro = piyasa[2].text
                speak("Euro is " + euro)
                print(euro)
        for i in SLEEP_STR:
            if text.count(i) > 0:
                speak("Sleep mode activated")
                os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep ")
        if text.count("liste yarat") > 0:
            liste_aç()
        if text.count("listeye yaz") > 0:
            listeye_yaz()
        # **************************AÇMA**********************************************
        if text.count("aç") > 0 and text.count("sesi") == 0 and text.count("kaç") == 0:
            speak("Yes sir")
            for i in WHATSAPP:
                if text.count(i) > 0:
                    webbrowser.open("https://web.whatsapp.com/")
            if text.count("youtube'u") > 0 or text.count("Youtube'u") > 0:
                webbrowser.open("https://youtube.com/")
            if text.count("netflix'i") > 0 or text.count("netflix'i") > 0:
                webbrowser.open("https://www.netflix.com/browse")
            if text.count("classroom u") > 0 or text.count("classroom") > 0:
                webbrowser.open("https://classroom.google.com/h")
            if text.count("ders sistemini") > 0:
                webbrowser.open("https://lms.gazi.edu.tr/")
            if text.count("sınav sistemini") > 0:
                webbrowser.open("https://gazi-sinav-lms.almscloud.net/Home/Login")
            if text.count("spotify") > 0 or text.count("spotify'ı") > 0:
                spotifyPath = "C:\\Users\\Murat\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
                os.startfile(spotifyPath)
            if text.count("valorant") > 0 or text.count("valorant'ı ") > 0:
                valorantPath = "C:\\Users\Murat\\Desktop\OYUN\\VALORANT"
                os.startfile(valorantPath)
            if text.count("cs yi") > 0 or text.count("counter aç") > 0:
                csPath = "C:\\Users\\Murat\\Desktop\\OYUN\\Counter-Strike Global Offensive"
                os.startfile(csPath)
            if text.count("discord") > 0 or text.count("discord'u") > 0:
                dcPath = "C:\\Users\\Murat\\Desktop\\PROGRAM\\Discord"
                os.startfile(dcPath)
            if text.count("olasılık hocasının notlarını") > 0 or text.count("olasılık notlarını"):
                webbrowser.open("https://drive.google.com/drive/folders/1RvmriC5va3kZEhskdoAEhE7xdLT0xeqY")
            if text.count("email") > 0 or text.count("gmail'i") > 0 or text.count("gmail") > 0:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            if text.count("udemy") > 0:
                webbrowser.open("https://www.udemy.com/")
            if text.count("google'ı") > 0 or text.count("google") > 0:
                webbrowser.open("https://www.google.com/")
            if text.count("çalışma alanımı") > 0 or text.count("günlüğü") > 0 or text.count("çalışma alanını") > 0:
                webbrowser.open("https://app.clickup.com/4600131/v/b/li/42560592")
            for phrases in CHESS_STR:
                if text.count(phrases) > 0:
                    speak("Which site do you want?")
                    answer4 = get_audio()
                    if answer4.count("farketmez") > 0 or answer4.count("chess") > 0:
                        webbrowser.open("https://www.chess.com/home")
                    if answer4.count("lichess") > 0:
                        webbrowser.open("https://lichess.org/")
            for i in INTEGRALSITE_STR:
                if text.count(i) > 0:
                    webbrowser.open("https://www.symbolab.com/solver/integral-calculator")
            for i in DCMUTE_STR:
                if text.count(i) > 0:
                    keyboard.press(Key.f9)
                    keyboard.release(Key.f9)
        # """*********************************************************************************"""
        if text.count("yüzdelerini") > 0 or text.count("yüzdeler") > 0:
            speak(f"memory %{psutil.virtual_memory()[2]} used")
            print(f"Memory %{psutil.virtual_memory()[2]} used...")
            speak(f"cpu %{psutil.cpu_percent(interval=1)} used")
            print(f"cpu %{psutil.cpu_percent(interval=1)} used...")
            speak("disk usage is {}".format(psutil.disk_usage("/")[3]))
            print("Disk usage is {}...".format(psutil.disk_usage("/")[3]))
        if text.count("bunu bana hatırlat") > 0 or text.count("bunu unutma") > 0:
            with open("memory.txt", "r+", encoding="utf-8") as file:
                speak("What you want to remember?")
                memory = get_audio()
                for i in memory:
                    file.write(i)
                file.write("\n")
        if text.count("hatırlamam gereken") > 0 or text.count("unutmamam gereken") > 0:
            with open("Memory/memory.txt", "r", encoding="utf-8") as file:
                speak(file.read())
        if text.count("ses ayarları") > 0 or text.count("sesi") > 0 or text.count("müziği") > 0:
            if text.count("kıs") > 0 or text.count("azalt") > 0:
                print("kıs")
                ses_kıs(25)
            if text.count("arttır") > 0 or text.count("çoğalt") > 0:
                print("aç")
                ses_aç(25)
            if text.count("kapat") > 0:
                print("kapat")
                ses_kıs(50)
            if text.count("fulle") > 0 or text.count("aç"):
                print("full")
                ses_aç(50)
        if text.count("ekranı değiştir") > 0 or text.count("ekran değiş") > 0 or text.count("ekranı değiş") > 0:
            keyboard.press(Key.alt)
            keyboard.press(Key.tab)
            keyboard.release(Key.alt)
            keyboard.release(Key.tab)
        if text.count("hava nasıl") > 0 or text.count("hava durumu") > 0:
            hava_durumu()
        if text.count("çeviri") > 0:
            translate()
        if text.count("alarm") > 0 and text.count("kur") > 0:
            speak("Alarm set")
            p1=threading.Thread(target=alarm_tanıma,args=[text])
            p1.start()


        if text.count("uyandır")>0 and text.count("beni"):
            speak("Alarm set")
            p1 = threading.Thread(target=alarm_tanıma, args=[text])
            p1.start()
            p1.join()

            while True:
                text=get_audio_withoutwriting()
                speak("Time is up sir, wake up")
                if text.count("tamam")>0 or text.count("kapat")>0 or text.count("sus")>0:
                    break


        if text.count("antrenman moduna geç") > 0:
            go = ""
            while go.count("bitti") == 0:
                speak("What do you want to do?")
                go = get_audio_withoutwriting()
                if go.count("kardiyo") > 0:
                    speak("when you are ready")
                    while True:
                        go = get_audio_withoutwriting()
                        if go.count("başlat") > 0 or go.count("go") > 0:
                            speak("Burpees for 1 minute")
                            speak("1, 2, 3, go")
                            countdown(60)  # 60
                            speak("move on to planck for 30 second")
                            time.sleep(2)
                            countdown(30)  # 30
                            speak("move on to high knees for 30 second")
                            countdown(30)  # 30
                            speak("move on to planck for 30 second")
                            countdown(30)  # 30
                            speak("leg raise, 20 times")
                            go = get_audio_withoutwriting()
                            if go.count("bitti") > 0:
                                speak("You have been amazing so far, sir")
                                break
        if text.count("sınav moduna geç") > 0:
            speak("War mode Activated")
            while True:
                yardım = get_audio_withoutwriting()
                if yardım.count("sınav bitti") > 0:
                    speak("I hope you have done well, sir")
                    break
                if yardım.count("olasılık hocasının notlarını") > 0 or yardım.count("olasılık notlarını"):
                    webbrowser.open("https://drive.google.com/drive/folders/1RvmriC5va3kZEhskdoAEhE7xdLT0xeqY")
                if yardım.count("çeviri") > 0:
                    translate()
                for i in INTEGRALSITE_STR:
                    if text.count(i) > 0:
                        webbrowser.open("https://www.symbolab.com/solver/integral-calculator")
                for i in DCMUTE_STR:
                    if text.count(i) > 0:
                        keyboard.press(Key.f9)
                        keyboard.release(Key.f9)
                if text.count("classroom u") > 0 or text.count("classroom") > 0:
                    webbrowser.open("https://classroom.google.com/h")
                if text.count("ders sistemini") > 0:
                    webbrowser.open("https://lms.gazi.edu.tr/")
                if text.count("sınav sistemini") > 0:
                    webbrowser.open("https://gazi-sinav-lms.almscloud.net/Home/Login")
                if text.count("spotify") > 0 or text.count("spotify'ı") > 0:
                    spotifyPath = "C:\\Users\\Murat\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
                    os.startfile(spotifyPath)
                for i in WHATSAPP:
                    if text.count(i) > 0:
                        webbrowser.open("https://web.whatsapp.com/")
                if text.count("youtube'u") > 0 or text.count("Youtube'u") > 0:
                    webbrowser.open("https://youtube.com/")
                if text.count("saat kaç") > 0 or text.count("Saati söyle") > 0:
                    hour_talk = "It is " + datetime.datetime.now().strftime("%X")
                    speak(hour_talk)
                if text.count("araştır") > 0 or text.count("internetten bak") > 0 or text.count("search for"):
                    if text.count("araştır") > 0:
                        text = text.replace("araştır ", "")
                        print(text)
                    if text.count("search") > 0:
                        text = text.replace("search for ", "")
                        print(text)
                    try:
                        print(wikipedia.summary(text, sentences=2))
                        speak("Do you want me to read it?")
                        read = get_audio()
                        if read.count("evet") > 0:
                            speak(wikipedia.summary(text, sentences=1))
                    except:
                        try:
                            wikipedia.set_lang('tr')
                            print(wikipedia.summary(text, sentences=2))
                            speak("I found it on Turkish resources.Do you want me to read it?")
                            read = get_audio()
                            if read.count("evet") > 0:
                                speak_t(wikipedia.summary(text, sentences=1))
                                os.remove("voice.mp3")
                        except:
                            speak("I could not find any information...")
                for words in SEARCH_STR:
                    if text.count(words) > 0:
                        if text.count("search at google") > 0:
                            text = text.replace("search at google ", "")
                        if text.count("search up google") > 0:
                            text = text.replace("search up google ", "")
                        if text.count("google'da arat") > 0:
                            text = text.replace("google'da arat ", "")
                        googlesearch(text)
                
                
