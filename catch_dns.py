import socket
import sys
import re

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 4445)
print("starting up on" + server_address[0] + " port " + str(server_address[1]))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from' + str(client_address))

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            data = data.decode()
            print('received ' + data)
            # 05:13:05.526843 IP 192.168.91.128.60683 > 192.168.91.2.53: 42108+ A? v1.addthisedge.com. (36)

            if not re.search("A?", data):
                print("clgt")
                continue
            print(data)

            if data:
                print('sending data back to the client')
                # connection.sendall(data)
            else:
                print('no more data from ' + str(client_address))
                break
            
    finally:
        # Clean up the connection
        connection.close()