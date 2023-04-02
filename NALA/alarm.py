import datetime
import time
import win10toast 
from win10toast import ToastNotifier
import pygame
import time
import threading 
n= ToastNotifier()



def alarm():
    alarm_hour = int(input("Set hour: "))
    alarm_minutes = int(input("Set minutes: "))
    am_pm = input("am or pm? ")
    print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")
    # time conversion
    # because datetime module returns time in military form i.e. 24 hrs format
    if alarm_hour == 12 and am_pm == 'pm':  # to convert pm to military time
         alarm_hour = alarm_hour
         print("alarm, has been set at {}:{} {} ".format(alarm_hour,alarm_minutes,am_pm))
  
       
    elif  am_pm == 'pm' :
        print("alarm, has been set at {} {} {} ".format(alarm_hour,alarm_minutes,am_pm))
        alarm_hour += 12
   
            
    elif  am_pm == 'am':  # to convert 12am to military time
        alarm_hour = alarm_hour
        print("alarm, has been set at {} {} {} ".format(alarm_hour,alarm_minutes,am_pm))
       

    else:
        return "Written in Wrong format  , please correct it  "
    
   

    while True:  # infinite loop starts to make the program running until time matches alarm time

        # ringing alarm + execution condition for alarm
        if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:
            print("\nIt's the time! ....")
            time.sleep(1)
            pygame.mixer.init()
            pygame.mixer_music.load("F:/working songs/Vaathi-Coming-MassTamilan.io.mp3")
            pygame.mixer_music.play()
            n.show_toast(title="Notification",msg="Getup buddy",icon_path='F:/py programs/JARVIS/py.ico',duration=50,threaded=True)

            for _ in range(600):
                time.sleep(0.1)
            pygame.mixer_music.fadeout(100)    
            time.sleep(1)
            break
alarm()
'''
import os
from playsound import playsound
import datetime

extracted_time = open('E:\\YouTube Channel\\YouTube - Jarvis\\How To Make Jarvis In Python\\Data.txt','rt')
time = extracted_time.read()
Time = str(time)

delete_time = open("E:\\YouTube Channel\\YouTube - Jarvis\\How To Make Jarvis In Python\\Data.txt",'r+')
delete_time.truncate(0)
delete_time.close()

def RingerNow(time):

    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis","")
    time_now = time_now.replace("set alarm for ","")
    time_now = time_now.replace("set ","")
    time_now = time_now.replace("alarm ","")
    time_now = time_now.replace("for ","")
    time_now = time_now.replace(" and ",":")

    Alarm_Time = str(time_now)

    while True:

        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_time == Alarm_Time:
            print("Wake Up Sir , It's Time To Work .")
            playsound("F:/working songs/Vaathi-Coming-MassTamilan.io.mp3")

        elif current_time>Alarm_Time:
            break

RingerNow(Time)
'''