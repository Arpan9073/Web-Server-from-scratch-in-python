
# A simple web server in python

## 🛠 Tech Stack

- **Language:** Python 3
- **Networking:** socket (TCP)
- **Protocol:** HTTP/1.1
- **Concepts Used:**
  - Socket Programming
  - TCP Client-Server Model
  - HTTP Request Parsing
  - File Handling
  - Basic Networking

---

## 📂 Project Structure
simple-python-http-server/<br>
│<br>
├── server.py<br>
├── frontend/<br>
   └── index.html<br>


---

## ⚙️ How It Works

1. Creates a TCP socket.
2. Binds to a local IP address and port.
3. Listens for incoming client connections.
4. Accepts HTTP requests.
5. Parses request headers manually.
6. Sends a valid HTTP response with status line and body.

---

## Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Run the server
```bash
python server.py
```
### Open in browser
type this in url bar
```
http://<your-local-ip>:4080
```
## 📋 Requirements

To run this project, you need:

- **Python 3.8+**
- A system capable of running Python (Windows / Linux / macOS)
- A web browser (Chrome, Firefox, Edge, etc.)
- (Optional) Devices connected to the same local network for cross-device testing

### 🔎 Check Python Version

```bash
python --version
```
