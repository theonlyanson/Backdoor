#To be placed on a hacker's computer

import socket

ip = " " # Put your ip address within the quotes
port = 4444

def main():
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  address = (ip.port)
  sock.bind(address)
  sock.listen(1)
  print("listening for connection on port" + str(port))
  conn , ipvictim = sock.accept()
  msg = "this is the message from server"
  conn.send(msg.encode())
  conn.close()

main()
