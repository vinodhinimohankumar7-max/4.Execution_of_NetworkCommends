import socket
import subprocess
import platform

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)
print("Server listening on port 8000...")
c, addr = s.accept()
print("Connected:", addr)

while True:
    command = c.recv(1024).decode().strip()
    if not command or command.lower() == 'exit':
        print("Client disconnected.")
        break

    try:
        # Run ANY command the client sends
        completed = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            shell=True
        )
        output = completed.stdout + (completed.stderr or "")
    except Exception as e:
        output = f"Command failed: {e}"

    c.sendall(output.encode('utf-8'))

c.close()
s.close()