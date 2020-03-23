import socket
tcp_ip = '10.0.0.54'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

s.connect((tcp_ip,23))



msg = s.recv(500)
print(msg.decode("ascii"))

 
