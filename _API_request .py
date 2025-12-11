import requests
import json

id = 6776334925
token = "8488594492:AAFqFtkDOVYeZGJObK-RKDmKwSAahvYz2t4"

sms = "hello user!"

path = f"https://api.telegram.org/bot{token}/sendMessage"

data ={
   'chat_id':id,
   'text':sms
}

send = requests.get(path,params=data)

print(send.json())

