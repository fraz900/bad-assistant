import speech_recognition as sr
import pyttsx3
import time
import sys
import requests
from threading import Thread
import multiprocessing
import wikipedia
import datetime
import re
import simpleaudio as sa
import getpass
import os
import random
import hashlib

engine = pyttsx3.init()
r = sr.Recognizer()
def say(words):
    engine.say(words)
    engine.runAndWait()
def hear():
    with sr.Microphone() as source:
        while True:
            try:
                audio_text = r.listen(source)
                statement = r.recognize_google(audio_text)
                break
            except:
                None
        return(statement)
def input1():
    with sr.Microphone() as source:
        while True:
            try:
                audio_text = r.listen(source)
                statement = r.recognize_google(audio_text)
                break
            except:
                None
        while True:
            message = "is",statement,"correct?"
            say(message)
            audio_text = r.listen(source)
            statement1 = r.recognize_google(audio_text)
            if "yes" in statement1 or "correct" in statement1:
                return(statement)
            else:
                say("ok, let's try that again")


def check_connected():
    try:
        r = requests.head("http://www.google.com", timeout=5)
        say("connected")
        return(True)
    except requests.ConnectionError as ex:
        say("not currently connected, please connect to wifi")
        return False

def date_time():
    x = datetime.datetime.now()
    return(x)

def timer(time1):
    print("timer started")
    time.sleep(time1)
    say("your timer has gone off")
    global timer_running
    timer_running = False

global timer_running
timer_running = False 
check_connected()
global playing
global restart
playing = False
restart = True
class user_details():
    def __init__(self):
        global restart
        try:
            file = open("user_details.txt","r")
            details = file.read()
            file.close()
            details = details.split("\n")
            self.name = details[0]
            self.keyword = details[1]
            self.password = details[2]
            restart = False
        except:
            None
        if restart:
            try:
                USER_NAME = getpass.getuser()
                music_path = r'C:\Users\%s\Music\protocol_music' % USER_NAME
                os.mkdir(music_path)
            except:
                None
            say("starting setup mode, please follow the instructions")
            with sr.Microphone() as source:
                a = False
                while True:
                    try:
                        say("Say your name")
                        audio_text = r.listen(source)
                        statement = r.recognize_google(audio_text)
                        self.name = statement
                        message = "is your name " + statement
                        say(message)
                        while True:
                            audio_text = r.listen(source)
                            statement = r.recognize_google(audio_text)
                            if "yes" not in statement and "correct" not in statement:
                                say("got it, let's try that again")
                                break
                            else:
                                file = open("user_details.txt","w")
                                self.password = hashlib.sha256("alpha sierra 11".encode()).hexdigest()
                                entry = (str(self.name)) + "\nprotocol \n" + str(self.password)+"\n"
                                file.write(entry)
                                file.close()
                                self.keyword = "protocol"
                                a = True
                                break
                        if a:
                            break
                    except Exception as e:
                        print(e)
                        say("there was an unknown error, please try again")
                say("you have completed all madatory setup, however, there are many protocols in this program that require extra setup to use.")
                say("please check the documentation to find instructions on this")
    def repr(self):
        message = "name:",self.name
        message1 = "keyword:",self.keyword
        message2 = "admin password:","REDACTED"
        say(message)
        say(message1)
        say(message2)

ud = user_details()
message = "hi there", ud.name, "let's get started"
admin = False
say(message)
while True:
    print("loop start")
    print(ud.keyword)
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=2)
            audio_text = r.listen(source)
            statement = r.recognize_google(audio_text)
            print(statement)
            run = True
        except Exception as e:
            print(e)
            run = False
        if run:
            if ud.keyword in statement:
                if "hi" in statement and "assassinate" not in statement:
                    say("Hope your having a great day!")
                    
                elif "help" in statement:
                    say("for settings go to settings, for account details head to account, for a full list of commands consult my documentation")
                    
                elif "setting" in statement:
                    while True:
                        say("what setting would you like help with")
                        audio_text = r.listen(source)
                        statement1 = r.recognize_google(audio_text)
                        if "delete" in statement1:
                            say("are you sure you wish to delete all account details?")
                            response = hear()
                            if "yes" in response or "correct" in response:
                                if admin:
                                    os.remove("user_details.txt")
                                else:
                                    say("please login to the admin account first")
                                break
                            else:
                                say("action cancelled")
                                break

                        elif "data" in statement1: 
                            ud.repr()
                            say("would you like to delete this data?")
                            response = hear()
                            if "yes" in response or "correct" in response:
                                os.remove("user_details.txt")
                                say("essential data removed, shutting down")
                                sys.exit()
                                
                        elif "keyword" in statement1:
                            say("what would you like your keyword to be?")
                            keyword = input1()
                            say("new keyword set")
                            file = open("user_details.txt","r")
                            content = file.read()
                            file.close()
                            content = content.split("\n")
                            content[1] = keyword
                            ncontent = "\n".join(content)
                            file = open("user_details.txt","w")
                            file.write(ncontent)
                            file.close()
                        elif "admin" in statement1 or "administrator" in statement1 and "password" in statement1:
                            say("would you like to change the administrator password?")
                            check = hear()
                            if "yes" in check or "correct" in check:
                                if admin:
                                    while True:
                                        say("what would you like your new password to be?")
                                        new = hear()
                                        response = "is",new,"correct?"
                                        say(response)
                                        check = hear()
                                        if "yes" in check or "correct" in check:
                                            file = open("user_details.txt","r")
                                            content = file.read()
                                            file.close()
                                            content = content.split("\n")
                                            new = hashlib.sha256(new.encode()).hexdigest()
                                            new = str(new)
                                            content[2] = new
                                            ncontent = "\n".join(content)
                                            file = open("user_details.txt","w")
                                            file.write(ncontent)
                                            file.close()
                                            say("password reset")
                                            break
                                        else:
                                            say("do you want to try again?")
                                            check = hear()
                                            if "yes" in check or "correct" in check:
                                                say("retrying")
                                            else:
                                                say("cancelling")
                                                break
                                else:
                                    say("please login to the administrator account first")
                            else:
                                say("ok, cancelling")
                        elif "network" in statement1:
                            a = check_connected()
                            if a:
                                say("would you like to disconnect?")
                                b = hear()
                                if "yes" in b:
                                    say("the program cannot run without wifi")
                                    time.sleep(1)
                                    say("shutting down")
                                    time.sleep(1)
                                    sys.exit()
                                else:
                                    say("ok, staying connected")
                        elif "account" in statement1:
                            say("head to the account section for account details")
                        elif "help" in statement1:
                            say("there is the: data settings, keyword settings, network settings and account deletion settings")
                        elif "back" in statement1:
                            say("back")
                            break
                        else:
                            say("sorry, we don't have an option for that")
                            
                elif "account" in statement:
                    ud.repr()

                elif "music" in statement:
                    if playing:
                        #consider adding controls outside of music section for ease of access?
                        say("would you like to stop the music, or skip a song?")
                        a = hear()
                        global play_obj
                        if "stop" in a:
                            #global play_obj
                            global stop
                            stop = True
                            play_obj.stop()
                            say("music stopped")
                            playing = False
                        elif "skip" in a:
                            play_obj.stop()
                            say("song skipped")
                        else:
                            say("action cancelled")
                    else:
                        say("playing music")
                        def play(file_names):
                            for name in file_names:
                                global stop
                                if stop:
                                    break
                                global play_obj
                                try:
                                    wave_obj = sa.WaveObject.from_wave_file(name)
                                    play_obj = wave_obj.play()
                                    play_obj.wait_done()
                                    playing = False
                                except:
                                    None
                            try:
                                say("playlist finished")
                            except:
                                None
                            playing = False
                        USER_NAME = getpass.getuser()
                        music_path = r'C:\Users\%s\Music\protocol_music' % USER_NAME
                        files = os.listdir(music_path)
                        ext = [".wav"]
                        music_files = []
                        for file in files:
                            if file[-4:] in ext:
                                file = music_path + "\\" + file
                                music_files.append(file)
                        stop = False
                        if "shuffle" in statement or "Shuffle" in statement:
                            music_files = random.sample(music_files, len(music_files))
                        t = Thread(target=play,args=(music_files,),daemon=True)
                        t.start()
                        playing = True
                        
                elif "timer" in statement:
                    if timer_running:
                        say("your timer is currently running")
                    else:
                        a = statement
                        number = int(re.search(r"\d+", a).group())
                        timer_running = True
                        Thread(target=timer,args=(number,)).start()
                        message = "your", number, "seconds timer has been started"
                        say(message)
                        
                elif "what" in statement or "who" in statement or "where" in statement:
                    querywords = statement.split()
                    stopwords = ["what","is","how","who",ud.keyword,"where"]
                    resultwords  = [word for word in querywords if word.lower() not in stopwords]
                    result = ' '.join(resultwords)
                    answer = wikipedia.summary(result,sentences=2)
                    say(answer)
                elif "admin" in statement or "administrator" in statement:
                    password = ud.password
                    say("say back to exit administrator login")
                    while True:
                        say("enter password")
                        check = hear()
                        check = check.lower()
                        attempt = hashlib.sha256(check.encode()).hexdigest()
                        if "back" in check:
                            break
                        elif password == attempt:
                            admin = True
                            say("administrator enabled")
                            break
                        else:
                            say("password incorrect, try again, or say back to exit login")
                elif "assassinate" in statement:
                    statement = statement.replace("assassinate","")
                    statement = statement.replace(ud.keyword,"")
                    message = "assassination commencing on",statement
                    say(message)
                    
                elif "shutdown" in statement:
                    say("shutting down")
                    time.sleep(3)
                    say("goodnight")
                    sys.exit()
        
                else:
                    say("sorry, I didn't understand that, please try again")
            
