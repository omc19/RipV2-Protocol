import socket

input0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input0.bind(('', 7003))

#output0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#output0.bind((socket.gethostname(), 7002))


while True:
    msg, address = input0.recvfrom(1024)
    msg = msg.upper()
    input0.sendto(msg, address)


