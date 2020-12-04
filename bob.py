
'For receiving messages as Bob'

import socket                
from my_a5_1 import decrypt, port

s = socket.socket()                   
s.connect(('127.0.0.1', port))  # localhost
message = s.recv(1024)
s.close()  

message = decrypt(message.decode())
print('Received message: ' + message + '\n')
