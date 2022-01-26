# my-first-codes
my first codes
#!/usr/bin/env python3

# ~ Bağımlılıklar
# ~  pip3 install SpeechRecognition
# ~ sudo apt-get install python3-pyaudio

import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from playsound import playsound
from gtts import gTTS
import os
import random
from selenium import webdriver
from googletrans import Translator
import googletrans
import cv2
from tkinter import Tk,PhotoImage,Button,Label
from bs4 import BeautifulSoup
import requests

pencere = Tk()
pencere.title("Astra135")
pencere.geometry("171x530")


r = sr.Recognizer()

def speak(text,dil='tr'):
    tts = gTTS(text=text,lang=dil)
    r = random.randint(1, 100000)
    file = 'audio-'+str(r)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def record():
    with sr.Microphone() as source:
        audio = r.record(source, duration=5)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
            print(voice)
        except sr.UnknownValueError:
            print('anlayamadım')
        except sr.RequestError:
            print('sistem çalışmıyor')
        return voice      
def hava():
    speak("hangi şehir için istiyorsunuz")
    print("hangi şehir için istiyorsunuz?")
    city = record()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&lang=tr&appid=70234438821740a1c41b2810a442cfe7"
    print("bilgiler toplanıyor...")
    json_data = requests.get(api).json()
    print("bilgiler toplanıyor...")
    condition = json_data['weather'][0]['main']
    print("bilgiler toplanıyor...")
    temp = int(json_data['main']['temp'] - 273.15)
    print("bilgiler toplanıyor...")
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    print("bilgiler toplanıyor...")
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    print("bilgiler toplanıyor...")
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
    print("bilgiler toplandı.")
    if condition == "Clouds":
        condition = "Bulutlu"
    if condition == "Clear":
        condition = "temiz"
    if condition == "Rain":
        condition = "yağmurlu"
    final_info = condition + "ve" + "\n" + str(temp) + "°C"
    final_data = "Basınç: " + str(pressure) + "bar" +"/n"+ "%" + "Nem: " + str(humidity) + "/n" + "Rüzgar Hızı: " + str(wind) + " km/saat" + "/n" + "Gün doğumu: " + sunrise + "/n" +"Gün batımı: " + sunset
    speak(city + "için bugün hava" + final_info)
def Nottut():
    yaz= open("dosya1.txt", "w")
    sesli = record()
    yaz.write(sesli)
    yaz.close()
    write = open("dosya1.txt", "r")
    speak(write.read() + "diye not tuttum")
    speak("sana hatırlatmamı istermisin")
    search = record()
    if "Evet" in search:
        os.system("alarm.py")
    if "Hayır" in search:
        speak("tamam")   
def ad():
    yaz= open("dosya.txt", "w")
    sesli = record()
    yaz.write(sesli)
    yaz.close()      
def eba_giris():
    url = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
    driver = webdriver.Chrome(url)
    speak("krom açıldı")
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/student.jsp")

    speak("T.C. kimliğinizi girin")
    tc = input("T.C.'nizi girin :")
    speak("Şifrenizi giriniz")
    sifre = input("Şifrenizi giriniz :")

    TCKN = driver.find_element_by_xpath('//*[@id="tckn"]')
    TCKN.click()
    TCKN.send_keys(tc)
    Sifre = driver.find_element_by_xpath('//*[@id="password"]')
    Sifre.click()
    Sifre.send_keys(sifre)
    Giris = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/form/div[5]/button")
    Giris.click()
    speak("ebaya giriş başarılı")
def kamera():
    speak("kamera açıldı")
    cam = cv2.VideoCapture(0)
    i=0
    while i<60:
        _, frame = cam.read()
        cv2.imshow("frame",frame)
        # ~ search= record()
        if cv2.waitKey(20) & 0xFF == ord("q"):
            speak("kamera kapatıldı")
            break
    speak("fotoğraf veya video çekeyim mi") 
    search = record()
    if "Hayır" in search:
        speak("tamam")       
    elif "Fotoğraf çek" in search:
        speak("kamera açıldı")
        cam = cv2.VideoCapture(0)
        sayac = 0
        while sayac<60:
            ret, frame = cam.read()
            cv2.imshow("kamera", frame)
            search = record()
            if not ret:
                speak("hata")
                print("hata")
            if cv2.waitKey(1)& 0xFF == ord("q"):
                speak("kamera kapatıldı")
                break
            # ~ elif "Fotoğraf çek"in search
            dosya_adi = 'resim/resim_{}.png'.format(sayac)
            cv2.imwrite(dosya_adi, frame)
            speak("fotoğrafını çektim")
            sayac +=1
        cam.release()
        cv2.destroyAllWindows()
    if "video çek" in search:
        speak("kamera açıldı")
        cam = cv2.VideoCapture(0)
        say = 0
        cv2.namedWindow("teknoupdate")
        fourrc = cv2.VideoWriter.fourcc(*'XVID')
        out = cv2.VideoWriter("resim/dronegri{}.avi".format(say), fourrc, 30.0,(640,480))
        while True:
            ret, frame = cam.read()
            cv2.imshow("teknoupdate", frame)
            out.write(frame)
            if not ret:
                speak("hata")
                print("hata")
            if cv2.waitKey(20) & 0xFF == ord("q"):
                speak("kamera kapatıldı")
                break
            say +=1
        cam.release()
        out.release
        cv2.destroyAllWindows()
def response(voice):
    if "Selamünaleyküm" in voice:
        print("Aleykümselam. Senin için ne yapabilirim ?")
        speak("Aleykümselam. Senin için ne yapabilirim ?")
    elif "Selam" in voice:
        print("Aleykümselam. Senin için ne yapabilirim ?")
        speak("Aleykümselam. Senin için ne yapabilirim ?")
    elif "Merhaba" in voice:
        print("Aleykümselam. Senin için ne yapabilirim ?")
        speak("Aleykümselam. Senin için ne yapabilirim ?")
    elif "Adımı kaydet" in voice:
        speak("adını ne olarak kaydedeyim")
        ad()
    elif "adımı değiştir" in voice:
        speak("adını ne olarak kaydedeyim")
        ad()
    elif "osuruk sesi" in voice:
        playsound("osuruk.mp3")
        speak("işte bu doğal gaz")
    elif "Benim adım ne" in voice:
        txt = open("dosya.txt", "r")
        speak("adını " + txt.read() + " olarak not aldım")
        speak("adını değiştirmek ister misin")
        search = record()
        if "Evet" in search:
            ad()
        if "Hayır" in search:
            speak("tamam")
    elif "not tut" in voice:
        Nottut()
    elif "şaka yap" in voice:
        os.system("python şaka.py")
    elif "çeviri"in voice:
        os.startfile("çevir.py")
        exit()
    elif 'nasılsın' in voice:
        print('iyiyim sen nasılsın')
        speak('iyiyim sen nasılsın')
    elif 'saat kaç' in voice:
        print(datetime.now().strftime('%H:%M:%S'))
        speak(datetime.now().strftime('%H:%M:%S'))
    elif 'arama yap' in voice:
        speak("ne araştırmak istiyorsunuz?")
        search=record()
        wikiurl = "https://tr.wikipedia.org/w/index.php?search=" + search

        r = requests.get(wikiurl)

        soup = BeautifulSoup(r.content,"html.parser") 

        veri = soup.find_all("div",{"class":"mw-parser-output"})

        for a in veri:
            sonuc = a.find_all("p")
            cikti = sonuc[0].text
            speak(cikti)
    elif 'haritadan ara' in voice:
        print('Ne aramak istiyorsun ? ', end=".")
        speak('Ne aramak istiyorsun ? ')
        search = record()
        url = 'https://www.google.com/maps/place/' + search
        webbrowser.get().open(url)
        print('%s için haritadan bulduklarım'% search)
        speak('%s için haritadan bulduklarım'% search)
    elif "YouTube'da ara" in voice:
        print('Ne aramak istiyorsun ? ', end=".")
        speak('Ne aramak istiyorsun ? ')
        search = record()
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
        print(search, ' için bulduklarım')
        speak('%s için bulduklarım' % search)
    elif 'İstanbul' in voice:
        speak("İstanbul, Türkiye'de yer alan şehir ve ülkenin 81 ilinden biri. Ülkenin en kalabalık, ekonomik, tarihi ve sosyo-kültürel açıdan önde gelen şehridir")
    elif 'görüşürüz' in voice:
        speak('görüşürüz')
        exit()
    elif "adın ne" in voice:
        speak("benim adım astra135")
    elif "Alarm kur" in voice:
        os.startfile("alarm.exe")
        exit()
    elif "eba'ya gir" in voice:
        eba_giris()
    elif "kamera" in voice:
        kamera()
        cv2.destroyAllWindows()
    elif "video çek" in voice:
        speak("kamera açıldı")
        cam = cv2.VideoCapture(0)
        say = 0
        cv2.namedWindow("teknoupdate")
        fourrc = cv2.VideoWriter.fourcc(*'XVID')
        out = cv2.VideoWriter("resim/dronegri{}.avi".format(say), fourrc, 30.0,(640,480))
        while say<60:
            ret, frame = cam.read()
            cv2.imshow("teknoupdate", frame)
            out.write(frame)
            if not ret:
                speak("hata")
                print("hata")
            if cv2.waitKey(2) == ord("q"):
                speak("kamera kapatıldı")
                break
            say +=1
        cam.release()
        out.release
        cv2.destroyAllWindows()

    elif "Hava bugün nasıl" in voice:
        hava()
    elif "dinimizde günah olan şeyler nedir" in voice:
        speak("Allah'ın kesinlikle sevmediği ve çirkin olarak saydığı büyük günahlar bulunmaktadır.Şirk Koşmak.Şirk koşmak Allah'ın en sevmediği en büyük günahlardandır.Zina Yapmak.İçki İçmek.Faiz.Büyü Yapmak.Yalancı Şahitlik Yapmak.Adam Öldürmek İntihar Etmek")
    elif "benimle ingilizce konuş" in voice:
        speak("how may ı help you",'en')
    elif "benimle Rusça konuş" in voice:
        speak("Chem ya mogu vam pomoch'?",'ru')
    elif "benimle Arapça konuş" in voice:
        speak("kayf'astatie almusaeadat",'ar')
    elif "dediğimi tekrarla" in voice:
        speak(voice + "dedin")       
    elif "kapat" in voice:
        os.system('shutdown -F')
    elif "beatbox" in voice:
        beatbox = 'beatbox.mp3'
        playsound(beatbox)
        speak("harika bir beatbox performansı") 
    elif "Şiir oku" in voice:
        wikiurl = "https://www.sabah.com.tr/fotohaber/yasam/cahit-zarifoglu-sozleri-ve-siirleri-en-guzel-kisa-uzun-cahit-zarifoglu-siirleri-ve-sozleri"

        r = requests.get(wikiurl)

        soup = BeautifulSoup(r.content,"html.parser") 

        veri = soup.find_all("div",{"class":"row topDetail"})
  
        for a in veri:
            sonuc = a.find_all("figcaption") 
            c = [1,2,3,4,5,6,7,8,9]
            r = random.choice(c)
            time.sleep(2)
            cikti = sonuc[r].text
            speak(cikti)
def micphone():

    voice = record()
    btn.config(bg="green")
    if voice:
        print(voice)
        response(voice)
def cevir():
    os.startfile("çevir.py") 
def saka():
    os.startfile("şaka.py")   
def bilgi():
    speak("ne araştırmak istiyorsunuz?")
    search=record()
    wikiurl = "https://tr.wikipedia.org/w/index.php?search=" + search
    r = requests.get(wikiurl)
    soup = BeautifulSoup(r.content,"html.parser") 
    veri = soup.find_all("div",{"class":"mw-parser-output"})

    for a in veri:
        sonuc = a.find_all("p")
        cikti = sonuc[1].text
        print(cikti)
        speak(cikti)             
def hesap():
	speak("işlem seçiniz")
	search = record()
	if "toplama" in search:
		speak("1.bileşen")
		bls1 = record() 
		speak("2.bileşen")
		bls2 = record()
		speak(int(bls1) + int(bls2))                     
def siirt():
    wikiurl = "https://www.sabah.com.tr/fotohaber/yasam/cahit-zarifoglu-sozleri-ve-siirleri-en-guzel-kisa-uzun-cahit-zarifoglu-siirleri-ve-sozleri"

    r = requests.get(wikiurl)

    soup = BeautifulSoup(r.content,"html.parser") 

    veri = soup.find_all("div",{"class":"row topDetail"})
  
    for a in veri:
        sonuc = a.find_all("figcaption") 
        c = [1,2,3,4,5,6,7,8,9]
        r = random.choice(c)
        time.sleep(2)
        cikti = sonuc[r].text
        speak(cikti) 
def yutub():
    print('Ne aramak istiyorsun ? ', end=".")
    speak('Ne aramak istiyorsun ? ')
    search = record()
    url = 'https://www.youtube.com/results?search_query=' + search
    webbrowser.get().open(url)
    print(search, ' için bulduklarım')
    speak('%s için bulduklarım' % search)
def tekerleme():
	tkr = ["şu köşe yaz köşesi şu köşe kış köşesi orta da su şişesi","dal sarkar kartal kalkar kartal kalkar dal sarkar"]
	tkrl = random.choice(tkr)
	speak(tkrl)
	 
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)
text_font= ("Boulder", 30, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 8

label = Label(pencere, font=text_font, bg=background, fg=foreground, bd=border_width)
label.pack()
digital_clock() 
       
imgfile = PhotoImage(file="mikrafon.png")
btn = Button(pencere,image=imgfile,command=micphone,bg="red") 
btn.pack()
btn1 = Button(pencere,text='                       Çeviri                       ',command=cevir)
btn1.pack()
btn2 = Button(pencere,text='                 bana bir fıkra anlat               ',command=saka)
btn2.pack()
btn3 = Button(pencere,text='                      arama yap                     ',command=bilgi)
btn3.pack()
btn4 = Button(pencere,text='                     hava durumu                    ',command=hava)
btn4.pack()
btn5 = Button(pencere,text="                    YouTube'da ara                  ",command=yutub)
btn5.pack()
btn6 = Button(pencere,text="                      şiir oku                      ",command=siirt)
btn6.pack()
btn7 = Button(pencere,text="                        Hesap                       ",command=hesap)
btn7.pack()
btn8 = Button(pencere,text="                      tekerleme                     ",command=tekerleme)
btn8.pack()
# ~ while True:
    # ~ speak("doğrulama protokolü adınız")
    # ~ search = record()
    # ~ if "Ben Ömercan" in search:
        # ~ break
    # ~ else:
        # ~ speak("giriş başarısız")
        # ~ speak("iki deneme hakkınız kaldı")
        # ~ search=record()
        # ~ if "Ben Ömercan" in search:
            # ~ break
        # ~ else:
            # ~ speak("giriş başarısız")
            # ~ speak("bir deneme hakkınız kaldı")
            # ~ search=record()
            # ~ if "Ben Ömercan" in search:
                # ~ break
            # ~ else:
                # ~ speak("sizi tanımıyorum")
                # ~ exit()

pencere.mainloop()
