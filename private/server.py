import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()


def handle_connection(c):
    c.send("Enter '1' to sign up, '2' to log in: ".encode())
    request = c.recv(1024).decode()

    if request == "1":
        # handle sign up
        c.send("Desired username: ".encode())
        username = c.recv(1024).decode()
        c.send("Desired password: ".encode())
        password = c.recv(1024).decode()
        password = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()

        cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        c.send("Sign up successful!".encode())
    else:
        # handle login
        c.send("Username: ".encode())
        username = c.recv(1024).decode()
        c.send("Password: ".encode())
        password = c.recv(1024).decode()
        password = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

        if cur.fetchall():
            c.send("Login Successful!".encode())
        else:
            c.send("Login Failure!".encode())



while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()
