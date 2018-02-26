#!/usr/bin/python3

"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import calculadora

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024
# Queue a maximum of 5 TCP connection requests
# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)
try:
	while True:
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('Request received:')
		bytes_received = recvSocket.recv(2048)
		request = str(bytes_received, 'utf-8')
		#Proceso peticion
		print(request)
		resource = request.split()[1]
		print("Resource:", resource)
		_, op1, operacion, op2 = resource.split('/')
		print(op1, operacion, op2)
		#Hago lo que me piden
		num1 = int(op1)
		num2 = int(op2)
		resultado = calculadora.funciones[operacion](num1, num2)
		#Respondo
		print('Answering back...')
		recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + str(resultado), 'utf-8'))
		recvSocket.close()
except KeyboardInterrupt:
	print("Closing binded socket")
mySocket.close() #Cierro el socket
