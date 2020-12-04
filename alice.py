
'For sending messages from Alice'

import socket
from my_a5_1 import encrypt, port

message = input('Enter message to send: ') or 'secret'  # if no input
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

# code is uploaded on GitHub
# https://github.com/vhpraneeth/python_A51
