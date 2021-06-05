
import requests
import schedule
import time
import datetime
import sys

mynumber = 3617396315
marielNumber = 9493455203
morningMessage = 'Good morning baby :) I am asleep right now, but dont worry Im dreaming about you. I hope you have a wonderful day.'

nightMessage =  'Good afternoon baby :) Im probably working out right now, but dont worry, all the girls staring cant have me'

hourToSend = 9 
delayToLoop = 300
endProgram = False
loopCnt = 0
alarm = datetime.time(9, 1, 1) #Hour, minute and second you want.

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : marielNumber,
        
        'message' : morningMessage,
        
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
    
    loopCnt += 1
    print("LOOP COUNT IS:")
    print(loopCnt)

    print("END of loop")
    
    if (endProgram) :
        print("CLOSING PROGRAM")
        quit()


#test
#while True: 
    #schedule.run_pending()
    #time.sleep(1)

