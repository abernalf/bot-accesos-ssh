
# -*- coding: utf-8 -*- 
import paramiko
import os
 


ssh_usuario  = 'pi' #Usuario desde el cual nos conectaremos (Usuario del pc)
ssh_clave    = 'raspberry' #Pass de ese pc
ssh_puerto   = 22 # O el puerto SSH que use nuestro servidor
comando      = 'ls' # el comando que vamos a ejecutar en el servidor
 
# Conectamos al servidor
z = 0
a = 116 #Ultimo numero de la IP desde el cual comenzamos 
while z == 0:
	ssh_servidor = "192.168.1."+str(a)
	print (ssh_servidor)
	try:
		conexion = paramiko.Transport((ssh_servidor, ssh_puerto)) #HAce ssh a la ip por el puerto
		conexion.connect(username = ssh_usuario, password = ssh_clave) #Login en esa dirección 
	
		canal = conexion.open_session() # Abrimos una sesión en el servidor
	 
		conexion.close()
		a = a + 1
		z = 1
	except:
		print "Acceso invalido"
		a = a + 1