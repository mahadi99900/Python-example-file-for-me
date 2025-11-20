import requests
import json

def get_time_from_api():
    response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Dhaka')
    data = json.loads(response.text)
    return data['datetime']

print(get_time_from_api())