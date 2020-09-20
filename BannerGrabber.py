#!/usr/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(str(s.resv(1024)).strip('b'))

def main():
    ip = input("Please ener the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

main()
