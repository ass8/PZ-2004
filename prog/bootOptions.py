#!/usr/bin/python
import os
from datetime import datetime

currentTime=datetime.now().strftime("%H:%M")
currentHour=int(datetime.now().strftime("%H"))
currentMinute=int(datetime.now().strftime("%M"))

def invalidInput():
    print("Invalid input, please try again.\n")
    quit()

def shutdown():
    print("\t1)Shutdown PC immediately\n\t2)Shutdown PC in the given time\n\t3)Shutdown PC after the given time\n\t4)Cancel planned shutdown")
    time=int(input("Select an option: "))
    if time<1 or time>4:
        invalidInput()
    elif time==1:
        if systemDetect=='nt':#windows
            os.system("shutdown /s /t 0")
        elif systemDetect=='posix':#linux
            os.system("sudo shutdown now")
    elif time==2:
        print("Current time: ",currentTime)
        hourValue=int(input("Enter an exact hour to shutdown PC (type (current_hour)--24): "))
        if hourValue<currentHour or hourValue>24:
            invalidInput()
        else:
            if hourValue-currentHour==1:
                secValue=(60-currentMinute)*60
            else:
                secValue=((hourValue-currentHour-1)*60+(60-currentMinute))*60
            print("Shutdown after (sec)",secValue)
            if systemDetect=='nt':#windows
                shutMain="shutdown /s /t "
                shutTime=str(secValue)
                shutFull=shutMain+shutTime
                os.system(shutFull)
            elif systemDetect=='posix':#linux
                shutMain="sudo shutdown -P +"
                shutTime=str(int(secValue/60))
                shutFull=shutMain+shutTime
                os.system(shutFull)
    elif time==3:
        secValue=int(input("After which number of (sec) shutdown the PC: "))
        if secValue<0:
            invalidInput()
        else:
            print("Shutdown after (sec)",secValue)
            if systemDetect=='nt':#windows
                shutMain="shutdown /s /t "
                shutTime=str(secValue)
                shutFull=shutMain+shutTime
                os.system(shutFull)
            elif systemDetect=='posix':#linux
                shutMain="sudo shutdown -P +"
                shutTime=str(int(secValue/60))
                shutFull=shutMain+shutTime
                os.system(shutFull)
    elif time==4:
        if systemDetect=='nt':#windows
            os.system("shutdown -a")
        elif systemDetect=='posix':#linux
            os.system("sudo shutdown -c")

def reboot():
    print("\t1)Reboot PC immediately\n\t2)Reboot PC in the given time\n\t3)Reboot PC after the given time\n\t4)Cancel planned reboot")
    time=int(input("Select an option: "))
    if time<1 or time>4:
        invalidInput()
    elif time==1:
        if systemDetect=='nt':#windows
            os.system("shutdown /r /t 0")
        elif systemDetect=='posix':#linux
            os.system("sudo shutdown -r now")
    elif time==2:
        print("Current time: ",currentTime)
        hourValue=int(input("Enter an exact hour to reboot PC (type (current_hour)--24): "))
        if hourValue<currentHour or hourValue>24:
            invalidInput()
        else:
            if hourValue-currentHour==1:
                secValue=(60-currentMinute)*60
            else:
                secValue=((hourValue-currentHour-1)*60+(60-currentMinute))*60
            print("Reboot after (sec)",secValue)
            if systemDetect=='nt':#windows
                shutMain="shutdown /r /t "
                shutTime=str(secValue)
                shutFull=shutMain+shutTime
                os.system(shutFull)
            elif systemDetect=='posix':#linux
                shutMain="sudo shutdown -r +"
                shutTime=str(int(secValue/60))
                shutFull=shutMain+shutTime
                os.system(shutFull)
    elif time==3:
        secValue=int(input("After which number of (sec) reboot the PC: "))
        if secValue<0:
            invalidInput()
        else:
            print("Reboot after (sec)",secValue)
            if systemDetect=='nt':#windows
                shutMain="shutdown /r /t "
                shutTime=str(secValue)
                shutFull=shutMain+shutTime
                os.system(shutFull)
            elif systemDetect=='posix':#linux
                shutMain="sudo shutdown -r +"
                shutTime=str(int(secValue/60))
                shutFull=shutMain+shutTime
                os.system(shutFull)
    elif time==4:
        if systemDetect=='nt':#windows
            os.system("shutdown -a")
        elif systemDetect=='posix':#linux
            os.system("sudo shutdown -c")

print("List of options:\n\t1)Shutdown\n\t2)Reboot")
option=int(input("Select an option: "))
systemDetect=os.name
if option<1 or option>2:
    invalidInput()
if option==1:#shutdown
    shutdown()
elif option==2:#Reboot
    reboot()