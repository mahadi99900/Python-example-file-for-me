import random
import qrcode

a = random.randint(1, 10000)
b = random.randint(1, 100000)

data = input("enter your about QR code something: ")

img = qrcode.make(data)

filename = f"{a} my qr code {b}.png"
img.save(filename)

print(f"your QR code saved by this name: {filename}")