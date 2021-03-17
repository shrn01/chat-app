import socket
import threading

def send(message):
	node.send(message.encode())

def recieve():
	while True:
		data = node.recv(1024).decode()
		print(data,end = '')

node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
node.connect(('157.46.238.33',3890))
print('connected')
thread = threading.Thread(target = recieve,daemon = True)
thread.start()

while True:
	message = input()
	send(message + '\n')