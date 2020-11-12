
'For receiving messages as Bob'

import socket                
from a51 import decrypt, port

s = socket.socket()                   
s.connect(('127.0.0.1', port)) 
message = s.recv(1024)
s.close()  

message = message.decode()
message = decrypt(message)
print(message)
print()
