import socket
import ssl
import tkinter as tk
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 5353
LOG_FILE = "query_log.txt"

# SSL context (no verification for testing)
context = ssl._create_unverified_context()

def resolve(event=None):
    query = entry.get().strip()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a domain or IP.")
        return

    try:
        with socket.create_connection((HOST, PORT)) as sock:
            with context.wrap_socket(sock, server_hostname=HOST) as ssock:
                ssock.sendall(query.encode())
                result = ssock.recv(1024).decode()
                output_var.set(f"🔍 Result: {result}")

                # Log query
                with open(LOG_FILE, "a") as log:
                    log.write(f"Query: {query} -> Response: {result}\n")

    except Exception as e:
        output_var.set("❌ Error: " + str(e))

# GUI Setup
root = tk.Tk()
root.title("DNS Resolver (TCP over SSL)")
root.geometry("450x250")
root.configure(bg="#f0f4ff")

# Title
tk.Label(root, text="DNS Resolver", font=("Helvetica", 18, "bold"), bg="#f0f4ff", fg="#333").pack(pady=10)

# Input
entry = tk.Entry(root, font=("Helvetica", 12), width=40, bd=2, relief=tk.SOLID)
entry.pack(pady=10)
entry.bind("<Return>", resolve)

# Button
tk.Button(root, text="Search", command=resolve, font=("Helvetica", 12, "bold"),
          bg="#4f8ef7", fg="white", activebackground="#3c6edb", width=10).pack()

# Output
output_var = tk.StringVar()
tk.Label(root, textvariable=output_var, font=("Helvetica", 12), bg="#f0f4ff", fg="#222",
         wraplength=400, justify="center").pack(pady=20)

root.mainloop()

