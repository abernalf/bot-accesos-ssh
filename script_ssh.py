# -*- coding: utf-8 -*- 
import paramiko
import os
import argparse

LIMIT = 255

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Python bot for accessing ssh hosts")
	parser.add_argument("user", help="username")
	parser.add_argument("password", help="user's password")
	parser.add_argument("network", help="network")
	parser.add_argument("begin_host", help="Host id in IP to start")
	parser.add_argument("command", help="Command to run in the server after connecting")
	args = parser.parse_args()
	user = args.user
	password = args.password
	network = args.network
	host = args.begin_host
	command = args.command
	
	port = 22

	# Conectamos al servidor
	done = False
	while not done:
		server = network + str(host)
		print (server)
		try:
			conexion = paramiko.Transport((server, port)) #HAce ssh a la ip por el puerto
			conexion.connect(username = user, password = password) #Login en esa dirección 
			canal = conexion.open_session() # Abrimos una sesión en el servidor
			conexion.close()
			host = str(int(host) + 1)
			z = True
		except:
			print "Acceso invalido"
			if int(host) == LIMIT:
				print("Limit")
				done = True
			else:
				host = str(int(host) + 1)
			