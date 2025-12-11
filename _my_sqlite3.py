import sqlite3

with open('hhhh.jpg',"rb") as f:
	pic_file = f.read()

conn = sqlite3.connect("my_data.db")
file = conn.cursor()

file.execute('''
CREATE TABLE IF NOT EXISTS user(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       age INTEGER,
       roll INTEGER,
       email TEXT,
       profile BLOB
)
''')
file.execute("INSERT INTO user (name,age,roll,email,profile) VALUES (?,?,?,?,?) ",('mahadi',18,30,'mahdi.bin.iqbal.x1@gmail.com',pic_file))

file.execute("select * from user")
conn.commit()


conn.close()