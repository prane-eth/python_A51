
'For sending messages from Alice'

import socket
from a5_1 import encrypt, port

message = 'secret'
message = input('Enter message to send: ')
message = encrypt(message)

s = socket.socket()
s.bind(('', port))
s.listen(5)
print('Socket is listening')

while True: 
    c, addr = s.accept()
    c.send(message.encode())
    print('Message sent')
    c.close()
