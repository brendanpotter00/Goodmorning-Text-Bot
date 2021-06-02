
import requests
import schedule
import time
import datetime
import sys

mynumber = 3617396315
marielNumber = 9493455203
endProgram = False
alarm = datetime.time(9, 1, 1) #Hour, minute and second you want.

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : marielNumber,
        'message' : 'Goodmorning baby :) Im asleep rn, but have a good day!',
        'key' : 'textbelt'
    })
    print (resp.json())

#main call
#schedule.every().day.at('09:00').do(send_message)

schedule.every(1).seconds.do(send_message)

#print('hello')
now = datetime.datetime.now()
print("the time is:")
print(now.hour)
hour = now.hour
minute = now.minute
second = now.second 

""" hour = 9 
minute = 16  """

#testing NOT NEEDED
def clock():
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

#clock()

while True or hour == 9 :
    if hour == 9 and minute > 15 :
        endProgram = True
        print("END IS TRUE")

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second

    print("beginning of loop")
    time.sleep(3) # 5minute delay
    print("after delay MIDDLE")
    if hour == 9 and minute < 15 :
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

