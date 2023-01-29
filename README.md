# SecureLogin
This repository contains a simple secure login system consisting of three Python files: `server.py`, `database.py`, and `client.py`.

## Server
The `server.py` file contains the logic for the server-side of the login system. It creates a socket to listen for incoming client connections, and uses the `sqlite3` module to connect to a database named `userdata.db`. This database contains a table `userdata` with three columns: `id`, `username`, and `password`.

When a client connects to the server, it prompts the client for a username and password, which it then hashes using SHA-256. The server queries the database to see if the entered credentials match any of the rows in the `userdata` table. If a match is found, the server sends a "Login Successful" message to the client. If not, the server sends a "Login Failure" message.

## Database
The `client.py` file contains the logic for the client-side of the login system. It connects to the server and prompts the user for a username and password. It then sends the entered credentials to the server for verification, and prints the response from the server to the user.

## Client
 1. Run the `database.py` file to create the userdata.db database and insert example data.
 2. Start the server by running the `server.py` file.
 3. Run the `client.py` file to connect to the server and attempt to log in.
