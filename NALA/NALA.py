'''              ***                 NALA : The Voice Assistant                        ***               '''
 
import pyttsx3  # module for speech recognition
import speech_recognition  as sr  
import datetime
import pyautogui
import time
from time import sleep
import webbrowser as wb
#import pywhatkit as wkit
import os

from yaml import compose_all



# To start the Speech engine
class Speech():
    def speak(self,audio):
        self.audio = audio
        engine  = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice" ,voices[0].id)
        engine.setProperty('rate' ,175)
        engine.say(self.audio)
        engine.runAndWait()
speech = Speech()

# Date and Time Function 
class Calender:
    def Time(self):
        Time = datetime.datetime.now().strftime("%I:%M %p")
        sleep(0.5)
        speech.speak("current,Time, {}".format(Time))
        print("\nCURRENT TIME : " ,Time)

    def date(self):
        Date = int(datetime.datetime.now().day)
        Month = int(datetime.datetime.now().month)
        year = int(datetime.datetime.now().year)                                                                         
        speech.speak("todays date ,{} , {} , {}".format(Date,Month,year))                                                                       
        print("\nDATE : ",Date,":",Month,":",year)      

    def day(self):
        Date = int(datetime.datetime.now().day)
        Month = int(datetime.datetime.now().month)
        year = int(datetime.datetime.now().year)
        day = datetime.datetime(year,Month,Date)
        print(day.strftime("\nTODAY: %A "))
        speech.speak(day.strftime("%A."))

    def month(self):
        Date = int(datetime.datetime.now().day)
        Month = int(datetime.datetime.now().month)
        year = int(datetime.datetime.now().year)
        day = datetime.datetime(year,Month,Date)
        print(day.strftime("\nMONTH :  %B"))
        speech.speak(day.strftime("%B"))

    #  Greet or Welcome Function
    def greet(self):
        import random
        hour = datetime.datetime.now().hour
        if( hour >= 4 and hour < 12) :
            speech.speak("good morning,sir.")
        elif hour >= 12 and hour < 15:
            speech.speak("Good After noon,sir.")
        elif hour >= 15 and hour < 18:
            speech.speak("Good Evening,sir!")
        elif hour >= 18   and hour <= 24:
            speech.speak("welcome Back,sir !")
        else:
            speech.speak("Early Good morning,sir!")
        #date(),Time(),day()
        l = ["Getting ready"  , 'Getting, online' , 'Getting started']    
        speech.speak(random.choice(l))
        sleep(1)
        print('You Can Command me By Saying " NALA "')
        speech.speak('done , [you can command me by saying nala')
calender = Calender()

# Speech - Recognition Function
#  Reading Voice Commands :

class VoiceCommands:
    def ActiveListening(self):
        r= sr.Recognizer()
        with sr.Microphone() as source :
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            print("\nListening ..... ")
            voice = r.listen(source)
            try:
                print("Processing .....")
                word =  r.recognize_google(voice)
                print("you said : " + word)
            except Exception as e:
                print("sorry, can You repeat again")
                speech.speak("sorry, can You repeat [ again") 
                self.ActiveListening()    
        return word
    
command = VoiceCommands()


                      
class Tasks:
# 1. Gmail
    def get_email_info(self):
        import Gmail
        print("\n************** E - MAIL ***************\n")
        print('1.NEW Id  \t     2.OLD  ID')
        speech.speak("IS it, New Mail or Old mail ")
        m = command.ActiveListening().lower()
        if "new" in m:
                speech.speak("please Enter the correct MAIL ID. ")
                new = input("Please Enter the Mail Id : ")
                speech.speak("do you want to save this Id in email list sir []")
                ans = command.ActiveListening().lower()
                if ans == "yes":
                    speech.speak("what's the name for yor reference sir.")
                    ans = command.ActiveListening().lower()
                    with open("A:\\py programs/NALA/Gmail-mails.txt" , 'a') as f:
                        f.write("\n"+ans + " " + new)
                    speech.speak("ok sir. saving it as {} in email list.".format(ans))
                    receiver = new
                    print(receiver)
                elif ans == "no": speech.speak("Okay [].")    

        elif "old" in m:
            speech.speak("Okay [Here are the list [you have. ")
            try:
                email = {}
                with open("A:/py programs/NALA/Gmail-mails.txt" , 'r+') as f:
                    for e in f:
                        key ,value = e.split()    
                        email[key] = value
                print(email)      
            except:pass      
            speech.speak("For Whom do you want send email?")
            name = input()
            if name in key:
                receiver = email[key]
                print(receiver)
                    
        print('What is the subject of your email?')
        speech.speak('What is the subject of your email?')
        subject = command.ActiveListening()

        print('Tell me the text in your email')
        speech.speak('Tell me the text in your email')
        message = command.ActiveListening()

        try: 
            Gmail.send_message(Gmail.service,receiver, subject, message)
            print('Your E-mail is Sent Successfully !!')
            speech.speak(' Your email is sent Successfully. ')
        except :
            print("\nFailure")
            speech.speak("mail not sent. please Try again .")    
            
        speech.speak('Do you want to send more mail? ')
        b = command.ActiveListening()
        if b == "yes":
            Tasks.get_email_info()
        elif b == "no":
            speech.speak("ok sir, returning to home !!")
    # to check how many measage from G-mail
    def check_message(self):
        import Gmail
        Gmail.check_mails(Gmail.service)
     
# 2. Screenshot
    def screenshot(self):
        name = int(round(time.time() * 1000))
        name = "C:/Users/arsha/Pictures/Screenshots/{}.png".format(name)
        img = pyautogui.screenshot(name)
        speech.speak("Done And Dusted.")    

# 3. Location 
    def locate(self,query):
        query = query.split()
        place= query[-1]
        speech.speak(f"according to google maps {place} lies here")
        wb.open_new_tab("https://www.google.com/maps/place/"+place)   

# 4. Serach Engine Function
    def Search_Engine(self,query):
        query = query.replace('search', '')
        query = query.replace('browse', '')
        chromepath ="C:/Program Files/Google/Chrome/Application/chrome.exe  %s"
        
        if 'google' in query:
            lst = ["in google about ", "google about " ,"in google ",'google ']    
            for _ in lst:
                query = query.replace(_, '')
            print(query)
            speech.speak("here are the result.")
            wkit.search(query)
        else :
            speech.speak("Opening {}, ".format(query))
            wb.get(chromepath).open_new_tab(query + '.com')    

# 5 . Playing on YouTube Function
    def plyt(self,query):
        list = ["can you play","on youtube",'play']
        for  i in list:
            query = query.replace(i,'')
        wkit.playonyt(query)

# 6. Weather
    def weather_data(self,query):
        import requests
        query = query.split()
        city  = query[-1]
        
        if "here" in city or "temperature" in city:
            city_name = "trichy"
        else:
            # Give city name
            city_name = city
            print(city_name)
        # Enter your API key here
        api_key = "b10b7b5f4a799532bdd05b3153b212e6"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + '&units=metric'

        response = requests.get(complete_url)

        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            if 'temperature' in query:
                print(" The Temperature in {} is = ".format(city_name) + str(current_temperature) + ' °C')
                speech.speak(" The Temperature in {} is  ".format(city_name) + str(current_temperature) + '°C')
        
            elif "humidity" in query:
                    print("humidity  = " +  str(current_humidity) + ' %') 
                    speech.speak("The humidity is around  " + str(current_humidity) + 'percent')
            else:
                speech.speak(" The Temperature in {} is  ".format(city_name) +
                            str(current_temperature) + '°C' +
                "\n and The atmospheric pressure is around " +
                            str(current_pressure) + 'hpa unit' +
                "\n plus The humidity is around  " +
                            str(current_humidity) + 'percent' +
                "\n and the weather outside will be.....  " +
                            str(weather_description))
                # print following values
                print(" The Temperature in {} is = ".format(city_name) +
                                str(current_temperature) + '°C' +
                    "\n Atmospheric pressure  = " +
                                str(current_pressure) + ' hpa unit' +
                    "\n Humidity  = " +
                                str(current_humidity) + ' %'
                    "\n Climate = " +
                                str(weather_description))
        
        else:
            print(" City Not Found ")

# 7. System Login Function
    def system(self,query):
    
        if "logout the system" in query or  "logout my system" in query:
            speech.speak("ok sir, logging out the system in 5 seconds.")
            for i in range(5,0,-1):speech.speak(i)
            sleep(1)  
            os.system("shutdown -l")
    
        elif "shutdown the system" in query or "shutdown my system" in query:
            speech.speak("ok sir, shutdowning the system in 5 sec.")
            for i in range(5,0,-1):speech.speak(i)
            sleep(1)
            os.system("shutdown /s /t 1")

        elif "restart the system" in query or "restart my system" in query:
            speech.speak("ok sir ,  restarting....the, system in 5 seconds.")
            for i in range(5,0,-1):speech.speak(i)
            sleep(1)
            os.system("shutdown /r /t 1")

# 8. Open Apps Function
    def open_apps(self,query):
        if ".com" in query or " dot com" in query:
            ch = "C:/Program Files/Google/Chrome/Application/chrome.exe  %s"
            if "udemy" in query:
                speech.speak("Opening udemy.")
                wb.get(ch).open_new_tab  ('https://www.udemy.com/home/my-courses/learning/')    
            
            elif "youtube" in query:
                speech.speak("Opening Youtube.")
                wb.get(ch).open_new_tab ('https://www.youtube.com') 
            
            else:    
                query = query.replace("open ", '')
                speech.speak("Opening {}, ".format(query))
                wb.get(ch).open_new_tab(query)
        else:        
            try: 
                path = "JARVIS/Apps-Softwares/"
                query = query.replace("open " ,'')  
                print("\n** Opening The Path Containing The Software ! **\n")
                print(path)
                os.chdir(path)
                os.startfile(query)
            except:
                try:
                    os.system(query)
                except:
                    speech.speak("Sorry. No results found. May be The Software is not located in the specific path")    
    
      
task = Tasks()


# 9. Intro
def intro(query):  
    if "introduce" in query:
        speech.speak("hey there! I'm  NALA [A virtual voice assistant , )Created by  (Arshath. " 
        + "[Basically [i'm not that advanced virtual assistant as my co-stars like, google or alexa" + 
        "[But my knowledge will definitely impress you! [I can do all the Basic needs of a laptop or a computer,"
        + "[I dont want you to be bored. [But  Do You want to know more? i'll help! , tell me yes or no? ")
        b = input()
        if "y" in b:
                speech.speak("since i'm a developing virtual assistant , i can do something which may be useful , that is,"
                +" (I can tell you all about in the calender ,like date , time , excetra. "
                +"I can remind you whenever you want , as you assign correct Attributes to me! "
                +"I can browse anything in google as u want. i can also send emails, check Mails (and  I can also check the weather accurately. "
                +"And, as I said i can do all the needs u want to do in a computing device manually. "
                +"So this is the basic introduction of myself, I hope you got it [Thank you.")
                sleep(1)     
        else:
            speech.speak("thanks, that saves my battery life a lot !")    
            
    else:
        speech.speak("Hello; my name is NALA. [Whats your name? ")
        ans = input()
        speech.speak(f"-hi -{ans}")


# 12 Notpad Function     TO seperate each folder for a topic (like list txt one folder, notes on fold)  _  to add,to remove,to append
'''def note():
    speech.speak("Please start saying yor notes")
    a = command().lower()
    speech.speak("WHat name would you prefer to save this file")
    b = command().lower()
    c = open("A:/py programs/JARVIS/{}.txt".format(b) , 'w+')
    c.write(a)
    speech.speak("file has been written and saved on your disk")
    c.close()
'''
     
# Tasks-Execution 

def ExecutionTasks(query):
    query = query.lower()
    if "day" in query:
        calender.day()
    elif "date" in query:    
        calender.date()
    elif  "time" in query:    
        calender.Time()
        
    elif "month" in query:    
        calender.month()  
    elif "name" in query or "introduce" in query or "intro" in query:
        intro(query)   
    elif "can you play {} on youtube".format(query) in query or "can you play" in query or "play" in query:
        task.plyt(query)
    elif 'search' in query or "browse" in query or 'google' in query :
        task.Search_Engine(query)        
    elif 'screenshot' in query:
        task.screenshot()
        task.locate(query)
    elif 'send mail' in query:
        task.get_email_info()
    elif 'weather' in query or 'climate' in query or "temperature" in query:
        task.weather_data(query)
    elif 'temperature' in query:
        task.weather_data(query)    
    elif 'humidity' in query:
        task.weather_data(query)    
    elif "logout the system" in query or "logout my system" in query:
        task.system(query)
    elif "shutdown the system" in query or "shutdown my system" in query:    
        task.system(query)      
    elif "restart the system" in query or "restart my system" in query:
        task.system(query)     
    elif "open" in query:
        task.open_apps(query)
    elif "who are you" in query or 'introduce' in query or "intro" in query:
        intro()    
    elif "send email" in query:
        task.get_email_info() 
    elif "check mail" in query:
        task.check_message()       
    elif "exit" in query:
        exit()    
    else: 
        speech.speak("sorry! I dont nderstand ! but I Try to give the Best results")
        
         

# MAIN
 
if __name__ =='__main__':
    while True:
        ExecutionTasks(input())
         
        