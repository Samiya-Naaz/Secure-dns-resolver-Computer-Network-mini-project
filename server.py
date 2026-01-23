import ssl
import socket
import time
import threading
from resolver import recursive_dns_lookup, reverse_dns_lookup

HOST = '127.0.0.1'
PORT = 5353

# SSL context setup
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='ssl/server.crt', keyfile='ssl/server.key')

# Function to handle individual client connections
def handle_client(conn, addr):
    print(f"[+] Connected: {addr}")
    try:
        data = conn.recv(1024).decode().strip()
        print(f"[>] From {addr}: {data}")

        if not data:
            conn.close()
            return

        if data.replace('.', '').isdigit():  # IP address
            result = reverse_dns_lookup(data)
        else:
            result = recursive_dns_lookup(data)

        conn.sendall(result.encode())

        # ✅ Log the query and result
        with open("query_log.txt", "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {addr[0]} - Query: {data} - Result: {result}\n")

    except Exception as e:
        print(f"[!] Error with {addr}:", e)
        conn.sendall(b"Error resolving request.")
    finally:
        conn.close()
        print(f"[*] Connection with {addr} closed")

# Create and bind plain socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"[+] Server listening on {HOST}:{PORT}...")

    while True:
        client_conn, client_addr = sock.accept()

        # Wrap each client connection with SSL
        ssl_conn = context.wrap_socket(client_conn, server_side=True)

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(ssl_conn, client_addr))
        thread.start()

