# Multi-Client Chat Application (Socket Programming)

## Overview

This project implements a **multi-client chat application using TCP socket programming**.
The system consists of a **central server** and multiple **clients** that communicate in real time over a network.

The server manages connected users, broadcasts messages, and maintains chat history.
Clients can join the chat, send messages, receive messages from others, and leave the chat using commands.

The project demonstrates concepts such as **client-server architecture, concurrency, protocol design, and reliable TCP communication**.

---

## Features

### Core Features

* Multi-client chat server using **TCP sockets**
* **Thread-per-client concurrency model**
* Real-time **message broadcasting**
* **Username system**
* **Join and leave notifications**
* Graceful disconnect using `/quit`

### Extra Features

* **Message timestamps**
* **User list command (`/users`)**
* **Persistent chat history (`chat.log`)**
* **Server logging**
* **Recent chat history displayed to new users**

---

## System Architecture

The system follows a **client–server model**.

* The **server** listens for incoming client connections.
* Each client connection is handled using a **separate thread**.
* Messages sent by a client are **broadcast to all other connected clients**.

```
             Chat Server
                 |
        ---------------------
        |        |         |
     Client1  Client2   Client3
```

---

## Communication Protocol

The application uses a simple text-based protocol.

| Command | Description                           |
| ------- | ------------------------------------- |
| JOIN    | Client sends username when connecting |
| MSG     | Regular chat messages                 |
| /users  | Shows list of connected users         |
| /quit   | Disconnect from chat                  |

Example messages:

```
[19:32:21] Nikhil: Hello
[19:32:40] Aman: Hi
```

---

## Project Structure

```
chat-app/
│
├── server/
│   └── server.py
│
├── client/
│   └── client.py
│
├── chat.log
├── README.md
└── Report.pdf
```

---

## Requirements

* Python 3.x
* Standard Python libraries only:

  * `socket`
  * `threading`
  * `datetime`

No external networking libraries are used.

---

## How to Run the Application

### 1. Start the Server

Open a terminal and run:

```
python3 server/server.py
```

Output example:

```
Server running on 127.0.0.1:5000
```

---

### 2. Start Clients

Open multiple terminals and run:

```
python3 client/client.py
```

Enter a username when prompted.

Example:

```
Enter your username: Nikhil
Connected to chat server
```

---

### 3. Chat Commands

| Command      | Action            |
| ------------ | ----------------- |
| message text | send chat message |
| `/users`     | list online users |
| `/quit`      | leave the chat    |

Example session:

```
Nikhil: Hello everyone
Aman: Hi
/users
Online users: Nikhil, Aman
/quit
```

---

## Logging and History

The server automatically records events in:

```
chat.log
```

Example log entries:

```
[19:32:04] Nikhil joined the chat
[19:32:21] Nikhil: Hello
[19:32:40] Aman: Hi
[19:33:10] Nikhil left the chat
```

New clients also receive the **recent chat history** when joining.

---

## Testing

The application was tested with:

* Multiple clients joining simultaneously
* Concurrent message sending
* Client disconnection using `/quit`
* Server stability with multiple threads
* Edge cases such as empty or repeated messages

---

## Concepts Demonstrated

* TCP socket programming
* Client-server architecture
* Multi-threaded server design
* Application-layer protocol design
* Network I/O handling
* Persistent logging and history

---

## Author

Nikhil Yadav
B.Tech Computer Science
