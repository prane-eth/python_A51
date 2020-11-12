
'For sending messages from Alice'

import socket
from a51 import encrypt, port

message = 'This is a message'
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
