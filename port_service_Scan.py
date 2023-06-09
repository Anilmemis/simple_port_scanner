#!/usr/bin/python
import socket
import os
import sys

def retBanner(ip,port):
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect((ip,port))
            banner = s.recv(1024)
            return banner
        except:
            pass
            

def checkVulns(banner,filename):
    f = open(filename,"r+")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is Vulnerable :" + banner.strip("\n"))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] File Doesnt Exist!")
            exit(0)
        if not os.access(filename,os.R_OK):
            print("[-] Access Denied!")
            exit(0)    
    else:
        print("[-] Usage: " + str(sys.argv[0]) + "<vuln filename>")
        exit(0)
    portlist = range(1,100) # change for yourself
    for x in range(135,139):# change for yourself
        ip = "1.1.1."+str(x) #enter the target ip adr or domain and up to range in change limitted
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                print ("[+]"+ ip + "/" + str(port) + " + " + str(banner))
                checkVulns(banner,filename)
                
main()
