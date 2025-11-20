import requests as r

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6DcX7hWp7gVUxJMsDKavmsYpY-NXHsFoepHj2Gmw_lw&s=10"

a = r.get(url)
b = a.content

with open("img.jpg","wb") as f:
	f.write(b)