
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

## 🌐 Network Access

This server can be accessed from other devices (such as mobile phones, tablets, or other computers) as long as:

- Both devices are connected to the **same local network (Wi-Fi/LAN)**.
- You use the server machine's **local IP address** (e.g., `192.168.x.x`) instead of `localhost`.

### ⚠️ Important Notes

- This works only within the same local network.
- Firewall settings may need to allow incoming connections on the specified port.
- This server is not exposed to the public internet.
