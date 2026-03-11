# ⌨️ Keyboard Event Logger (For Learning & Security Research)

> “Not all heroes wear capes… some just log key events.” 🕵️‍♂️

Welcome to my **Keyboard Event Logging Lab Project** — a small cybersecurity learning project that explores:

* How keyboard events can be captured programmatically
* How systems communicate using a **client–server architecture**
* How logs can be **sent asynchronously without blocking the main process**

This project is **for educational purposes only** and demonstrates how such systems work so that developers and security enthusiasts can better understand and defend against them.

---

# 📦 Project Structure

```
keylogger/
│
├── host/
│   └── server.py
│
└── target/
    ├── logger.py
    ├── sender.py
    └── logs.txt
```

### 🖥 Host Machine

Contains the **server** responsible for receiving logs.

```
server.py
```

The server:

* Listens for incoming connections
* Receives log data
* Prints or stores received information

Think of it as the **log collector**.

---

### 💻 Target Machine

Contains the components that generate and send logs.

```
logger.py
sender.py
logs.txt
```

#### `logger.py`

Responsible for:

* Capturing keyboard events
* Writing them to `logs.txt`

#### `sender.py`

Responsible for:

* Reading the log file
* Sending the data to the host server

The logger and sender are **separate to avoid blocking**:

```
Keyboard capture → write to file
Sender process   → send logs independently
```

This keeps the logging process **smooth and responsive**.

---

# 🚀 How To Run

### 1️⃣ Start the Host Server

On the **host machine**:

```bash
python server.py
```

The server will begin **listening for incoming log data**.

---

### 2️⃣ Run the Logger

On the **test machine**:

```bash
python logger.py
```

This will start recording keyboard events to:

```
logs.txt
```

---

### 3️⃣ Start the Sender

In another terminal:

```bash
python sender.py
```

This reads from `logs.txt` and sends logs to the host server.

---

# ⚙️ Why Separate Logger and Sender?

If logging and sending happened in the same script:

```
capture → send → wait → capture
```

This could cause **blocking delays**.

By separating them:

```
logger.py → writes logs
sender.py → sends logs
```

The system becomes **asynchronous and smoother**.

---

# 🧠 What This Project Demonstrates

* Python networking basics
* Client–server communication
* File-based logging systems
* Handling asynchronous processes
* Understanding how monitoring software works

This knowledge is **important for cybersecurity defenders**, penetration testers, and developers.

---

# ⚠️ Disclaimer

This project is intended **strictly for educational and research purposes**.

Do **NOT** use this software:

* On devices you do not own
* On systems without **explicit permission**
* For surveillance or malicious activity

Unauthorized monitoring of devices or users may be **illegal** and unethical.

The author takes **no responsibility** for misuse of this code.

---

# 🧑‍💻 Author

Built while exploring **Python, system hooks, and networking**.

If you’re learning cybersecurity too:

⭐ Star the repo
🍴 Fork it
🧠 Break it and learn from it

---

# ☕ Final Words

Remember:

> With great scripting power comes great responsibility.

Now go build cool (and ethical) stuff. 🚀
