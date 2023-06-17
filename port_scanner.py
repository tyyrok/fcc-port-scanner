#!/usr/bin/python3

import socket
from common_ports import ports_and_services
import re

def get_open_ports(target, port_range, verbose_mode = False):
    open_ports = []

    
    regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    result = regex.match(target)
    if not result:
        try:
            address = socket.gethostbyname(target)
            url_name = target
        except socket.gaierror as ex:
            print(ex)
            return('Error: Invalid hostname')
    else:
        try:
            url_name = socket.gethostbyaddr(target)[0]
            address = target
        except socket.gaierror as ex:

            print(ex)
            return("Error: Invalid IP address")
        except Exception as ex:
            print(ex)
            url_name = ''
            address = target

    print(address, url_name)

    for port in range(port_range[0], port_range[1] + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        #print(target, port)
        try:
            if not s.connect((target, port)):

                open_ports.append(port)
        
        except Exception as ex:
            #print(ex)
            pass

        s.close()

    #print(open_ports, verbose_mode)

    if verbose_mode:

        if not url_name:
            outString = 'Open ports for ' + str(address)+ '\n' 
        else:
            outString = 'Open ports for ' + str(url_name) + ' (' + str(address) +  ')\n' 
        #print(url)
        #outString = 'Open ports for ' + str(url) + ' (' + str(target) +  ')\n' 
        outString += 'PORT     SERVICE\n'

        for i in range(len(open_ports) -1):
            serviceStr = ''
            if open_ports[i] in ports_and_services:
                serviceStr = ports_and_services[open_ports[i]]

            numSpaces = 7 if len(str(open_ports[i])) == 2 else 6 
            outString += str(open_ports[i]) + " " * numSpaces + str(serviceStr) + '\n'

        serviceStr = ports_and_services[open_ports[(len(open_ports) - 1)]]

        numSpaces = 7 if len(str(open_ports[len(open_ports) - 1])) == 2 else 6
        outString += str(open_ports[len(open_ports) - 1]) + " " * numSpaces + str(serviceStr)


        #print(outString)
        return(outString)

    
    return(open_ports)

#print(get_open_ports("104.26.10.78", [440, 450], True))
#'Open ports for 104.26.10.78\nPORT     SERVICE\n443      https'
print(get_open_ports("137.74.187.104", [440, 450], True))
#: Expected 'Error: Invalid IP address'
#print(get_open_ports("scanme.nmap.org", [20, 80], False))
# Lists differ: [22] != [22, 80]
#print(get_open_ports("scanme.nmap.org", [20, 80], True))
#print(get_open_ports("266.255.9.10", [22, 42], False))
#print(get_open_ports("scanme.nmap.org", [22, 42], False))

#'Open[21 chars]p.org (45.33.32.156)\nPORT     SERVICE\n22    [17 chars]http'
#resolved