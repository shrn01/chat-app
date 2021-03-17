import socket
import threading

def send(message):
    global connection
    connection.send(message.encode())

def recieve():
    while True:
        data = connection.recv(1024).decode()
        print(data,end = '')

node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
node.bind(('127.0.0.1',3890))
node.listen(5)
connection, address = node.accept()
print('recieved connection from',address)
thread = threading.Thread(target = recieve,daemon = True)
thread.start()

while True:
    message = input()
    send(message + '\n')

