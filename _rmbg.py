from rembg import remove
from PIL import Image
import random
a = random.randint(1,10000)
b = random.randint(1,10000)
input_path = input("enter your file name; ")
output_path = f"{a}_bg_removed_{b}.png"
input_img = Image.open(input_path)
output_img = remove(input_img)
output_img.save(output_path)
print("your filr saved by this name; {output_path}")