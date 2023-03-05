from tkinter import *
import time
import datetime
from pygame import mixer

root = Tk() 
root.title('Alarm-Clock') 

def setalarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if alarmtime != "::":
        alarmclock(alarmtime) 

def alarmclock(alarmtime):
    alarm_on = True
    while alarm_on:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alarmtime:
            Wakeup = Label(root, font = ('arial', 20, 'bold'),
                text="____wake up_____",bg="orange",fg="black")
            Wakeup.grid(row=6,columnspan=3)
            print("wake up!")
            mixer.init()
            mixer.music.load(r'D:\alarm-clock-short-6402.mp3')
            mixer.music.play()
            alarm_on = False
            break

def stop_alarm():
    mixer.music.stop()
    root.quit()

hrs = StringVar()
mins = StringVar()
secs = StringVar()

greet = Label(root, font = ('arial', 20, 'bold'),
    text="Take a short nap!")
greet.grid(row=1,columnspan=3)

hrbtn = Entry(root, textvariable=hrs, width=5, font=('arial', 20, 'bold'))
hrbtn.grid(row=2,column=1)

minbtn = Entry(root, textvariable=mins, width=5, font=('arial', 20, 'bold'))
minbtn.grid(row=2,column=2)

secbtn = Entry(root, textvariable=secs, width=5, font=('arial', 20, 'bold'))
secbtn.grid(row=2,column=3)

setbtn = Button(root, text="set alarm", command=setalarm, bg="DodgerBlue2", fg="white", font=('arial', 20, 'bold'))
setbtn.grid(row=4,columnspan=3)

timeleft = Label(root, font=('arial', 20, 'bold')) 
timeleft.grid()

stopbtn = Button(root, text="stop alarm", command=stop_alarm, bg="red", fg="white", font=('arial', 20, 'bold'))
stopbtn.grid(row=5, columnspan=3)

mainloop()
