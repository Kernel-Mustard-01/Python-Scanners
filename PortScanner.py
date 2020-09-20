#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP: ")
port = int(input("Enter Port: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("This port is closed")
    else:
        print("This port is open")

portScanner(port)

#This is gor a git test