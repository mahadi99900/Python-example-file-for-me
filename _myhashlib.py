import hashlib

data1 = input("enter your password: ")
data2 = input("confirm your password: ")

hash_data1 = hashlib.md5(data1.encode())
hash_data2 = hashlib.md5(data2.encode())

hash1 = hash_data1.hexdigest()
hash2 = hash_data2.hexdigest()

chack = hash1 == hash2

if chack == False:
	print("wrong password")
	print(f"your frist password hash is :{hash1}\nyour second password hash is {hash2}")

else:
	print("correct password")
	
	


