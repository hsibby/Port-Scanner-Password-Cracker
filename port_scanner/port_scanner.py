#!/usr/bin/python3
import socket
from termcolor import colored

ip = input("Enter the ip: ")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(1, 10000):
    if s.connect_ex((ip, i)) == 0:
        print("Port ", i, colored("[ OPEN ]", 'green'))
