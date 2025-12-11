import requests

url = "http://localhost:12345/"

def get_info():
	response = requests.get(url)
	if response.status_code == 200:
		main_data = response.json()
		print(main_data)
	else:
		print(f"error by {response.status_code}")
		
get_info()