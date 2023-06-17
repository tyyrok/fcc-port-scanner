#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

def get_open_ports(target, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        print(target, port)
        if not s.connect_ex((target, port)):
            open_ports.append(port)
        else:
            print("Closed")

    return(open_ports)

print(get_open_ports("209.216.230.240", [440, 445]))
#print(get_open_ports("www.stackoverflow.com", [79, 82]))