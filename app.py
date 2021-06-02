import credentials import number
import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : number,
        'message' : 'Goodmorning baby :) Im asleep rn. Have a good day!',
        'key' : 'textbelt'
    })
    print (resp.json())

schedule.every().day.at('09:00').do(send_message)