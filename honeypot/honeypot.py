import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222
LOG_FILE = "honeypot.log"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(5)

print(f"[+] Honeypot listening on port {PORT}")
connection_count = 0
print("[+] Waiting for connections...")

while True:
   client, address = server.accept()
   connection_count += 1

   client.sendall(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0\r\n")

   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   source_ip, source_port = address

   print(f"[!] Connection #{connection_count} from {source_ip}:{source_port}")

   try:
      client.settimeout(5)
      data = client.recv(1024)

      if data:
         message = data.decode("utf-8", errors="replace").strip()
      else:
         message = "<no data>"

   except socket.timeout:
      message = "<timeout>"

   log_entry = (
      f"Connection #{connection_count} | "
      f"{timestamp} | "
      f"Source: {source_ip}:{source_port} | "
      f"Data: {message}\n"
   )

   with open(LOG_FILE, "a") as log:
      log.write(log_entry)

   print(f"[+] Logged: {log_entry.strip()}")

   client.close()
