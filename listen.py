import socket
import time

UDP_IP = "192.168.31.173" # 设置为本机IP
UDP_PORT = 3333 # 默认端口

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print('{:-^100}'.format(''))
print('Start listen')
print('{:-^100}'.format(''))

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Time: {time.ctime()}")
    print(f"Port: {UDP_PORT}")
    print(f"Received message: {data[:10]}... from {addr}") # 只展示了广播信息的前10位
    print('{:-^100}'.format('')) 

