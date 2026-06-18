# Secure DNS Resolver 🔐
### Computer Networks Mini Project — 4th Semester, PES University

> A working DNS resolver with SSL/TLS encryption, built in Python with a GUI client.  
> Runs on Linux. Built solo as part of CN coursework.

---

## 🌐 What is this?

Traditional DNS queries are sent in **plaintext** — anyone on the network can intercept and read them (DNS sniffing). This project implements a **secure DNS resolver** that encrypts DNS communication using **SSL/TLS**, preventing eavesdropping and tampering.

---

## ✨ Features

- 🔒 **SSL/TLS encrypted DNS resolution** — queries and responses are encrypted end-to-end
- 🌍 **Domain to IP resolution** — resolves domain names securely
- 📡 **Supports UDP and TCP** — flexible protocol handling
- 🖥️ **GUI client** — user-friendly interface via `client_gui.py`
- 💾 **DNS caching** — `cache.json` stores resolved queries for faster repeat lookups
- 📝 **Query logging** — logs DNS queries for monitoring and debugging

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Security | SSL/TLS (OpenSSL) |
| Transport | UDP + TCP sockets |
| GUI | Python GUI (Tkinter) |
| Caching | JSON-based cache |
| Platform | Linux |

---

## 📁 Project Structure

```
Secure-dns-resolver/
│
├── resolver.py        # Core DNS resolution logic
├── server.py          # DNS server with SSL/TLS
├── client_gui.py      # GUI client for DNS queries
├── real.py            # Real DNS forwarding logic
├── cache.json         # DNS cache storage
├── ssl/               # SSL certificates and keys
└── .gitignore
```

---

## ⚙️ How to Run (Linux)

**1. Clone the repository**
```bash
git clone https://github.com/Samiya-Naaz/Secure-dns-resolver-Computer-Network-mini-project.git
cd Secure-dns-resolver-Computer-Network-mini-project
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the DNS server**
```bash
python server.py
```

**4. Launch the GUI client**
```bash
python client_gui.py
```

> ⚠️ **Note:** Runs on Linux. Windows not supported due to SSL socket handling differences.

---

## 🔐 How SSL/TLS Works Here

```
Client (client_gui.py)
       |
       | SSL/TLS encrypted query
       ↓
DNS Server (server.py)
       |
       | Forwards to real DNS resolver
       ↓
  resolver.py → cache.json (if cached, return directly)
       |
       ↓
  Response encrypted back to client
```

Without SSL, DNS queries look like:
```
Query: "what is google.com?" → visible to anyone on network
```
With SSL:
```
Query: [encrypted] → only server can read it
```

---

## 💡 Why This Matters

- Prevents **DNS spoofing** and **man-in-the-middle attacks**
- Protects **user privacy** — ISPs can't log your DNS queries
- Foundation for **DNS-over-TLS (DoT)** — a real industry standard used by Cloudflare (1.1.1.1) and Google (8.8.8.8)

---

## 🧠 Concepts Demonstrated

- Socket programming in Python (UDP + TCP)
- SSL/TLS certificate generation and usage
- DNS protocol fundamentals
- Client-server architecture
- Caching mechanisms

---

## 👩‍💻 Author

**Samiya Naaz** — Solo Project  
4th Semester, CSE, PES University Bangalore

---

*Computer Networks Mini Project | PES University | 2024*
