import socket
import ssl
from datetime import datetime

HOST = '192.168.64.108'
PORT = 5353
LOG_FILE = "query_log.txt"

# Create SSL context without verification (for testing)
context = ssl._create_unverified_context()

def log_query(query, response):
    with open(LOG_FILE, "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] Query: {query} -> Response: {response}\n")

while True:
    query = input("Enter domain or IP to resolve (or type 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        print("👋 Exiting client.")
        break

    protocol = input("Choose protocol (TCP only supported): ").strip().lower()
    if protocol != 'tcp':
        print("⚠️ Only TCP is supported with SSL in this setup.\n")
        continue

    try:
        with socket.create_connection((HOST, PORT)) as sock:
            with context.wrap_socket(sock, server_hostname=HOST) as ssock:
                ssock.sendall(query.encode())
                result = ssock.recv(1024).decode()
                print("✅ Response:", result, "\n")
                log_query(query, result)
    except Exception as e:
        error_msg = f"❌ Error: {e}"
        print(error_msg + "\n")
        log_query(query, error_msg)

