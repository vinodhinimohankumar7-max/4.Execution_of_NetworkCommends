import socket

s = socket.socket()
s.connect(('localhost', 8000))

print("Connected. Type any network command (ipconfig, ping, etc.) or 'exit'.")

while True:
    cmd = input("Enter command: ").strip()
    if not cmd:
        continue

    s.send(cmd.encode('utf-8'))
    
    if cmd.lower() == "exit":
        print("Exiting...")
        break

    output = s.recv(65536).decode()
    print("\n----- RESULT -----")
    print(output)
    print("------------------\n")

s.close()