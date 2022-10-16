#This script has to be placed on a victims computer

import socket

ip = " " # Insert your server-ip address within the quotes.
port = 4444

def main():
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  address = (ip,port)
  sock.connect(address)
  
  msg = sock.recv(1024)
  
  print(msg.decode())
  sock.close()

main()
