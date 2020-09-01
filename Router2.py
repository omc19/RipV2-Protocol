import socket

input0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input0.bind(('', 7004))

output0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:


while True:
    msg = input('Type your message: ')

    output0.sendto(msg.encode(), ('', 7003))

    data, server = output0.recvfrom(1024)
    print(data.decode())
