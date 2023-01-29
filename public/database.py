import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "Ekagra", hashlib.sha256("EkagraPass".encode()).hexdigest()
username2, password2 = "Meher", hashlib.sha256("MeherPass".encode()).hexdigest()
username3, password3 = "Nevaan", hashlib.sha256("NevannPass".encode()).hexdigest()
username4, password4 = "Shreyaan", hashlib.sha256("ShreyaanPass".encode()).hexdigest()


cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()




