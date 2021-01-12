#!/usr/bin/env python

import socket

send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recvIp = "192.168.80.131"
recvPort = 8484
toSendIp = "192.168.80.132"
toSendPort = 8484

recv.bind((recvIp, recvPort))

while True:
    send.sendto((input("Enter msg: ").encode()), (toSendIp, toSendPort))
    x = recv.recvfrom(1024)
    clientip = x[1][0]
    msg = x[0].decode()
    print(clientip + " :" + msg)