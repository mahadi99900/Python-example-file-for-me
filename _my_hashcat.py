import hashlib

p_dict = [
    "mahadi",
    "hasan",
    "mahmud"
]

hash_data = "aca41e5ea7b8f650de6451323120b854"

for p in p_dict:
	data = p.encode()
	d_data = hashlib.md5(data)
	main_data = d_data.hexdigest()
	if main_data == hash_data:
		print(f"password matched by {p}")
		break
else:
	print('No match found')

