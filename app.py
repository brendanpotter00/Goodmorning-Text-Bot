
import requests
import schedule
import time
import datetime
import sys

mynumber = 3617396315
marielNumber = 9493455203
hourToSend = 9
delayToLoop = 300
endProgram = False
alarm = datetime.time(9, 1, 1) #Hour, minute and second you want.

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : marielNumber,
        'message' : 'Good afternoon baby :) Im testing my program, but have a good rest of your day!',
        'key' : 'textbelt'
    })
    print (resp.json())

#main call
#schedule.every().day.at('09:00').do(send_message)

schedule.every(3).seconds.do(send_message)

#print('hello')
now = datetime.datetime.now()
print("the time is:")
print(now.hour)
hour = now.hour
minute = now.minute
second = now.second 

""" hour = 9 
minute = 16  """

""" #testing NOT NEEDED
def clock():
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

#clock() """

while True or hour == hourToSend :
    if hour == hourToSend and minute >= 59 :
        endProgram = True
        print("END IS TRUE")

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second

    print("beginning of loop")
    time.sleep(delayToLoop) # 5 minute delay
    print("after delay MIDDLE")
    if hour == hourToSend and minute <= 59 :
        print("SENDING TEXT")
        schedule.run_pending()
    
    print("END of loop")
    
    if (endProgram) :
        print("CLOSING PROGRAM")
        quit()


#test
#while True: 
    #schedule.run_pending()
    #time.sleep(1)

