#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importo las dependencias necesarias para el script
import dns.resolver
import dns.reversename
import getopt, sys

#Variables globales que luego usaré en la clase chee
#Pido los dos objetivos por consola
host1 = raw_input("Introduce el primer host por favor: ")
host2 = raw_input("Introduce el segundo host por favor: ")

#A continuacíon los meto en un array para posterior uso en cada clase
arr = []
arr.append(host1)
arr.append(host2)
myresolver = dns.resolver.Resolver()

class chee(object):
	def __init__(self, arr):
		super(chee, self).__init__()#Recibo las dos "variables" y las "almaceno" con la palabra reservada self
		self.arr        = arr
		self.myresolver = myresolver

#En esta función capturo todas las ips correspondientes cada ns
	def ipv4(arr, myresolver):
		for hosts in arr:
		 	try:
		 	 	res=myresolver.query(hosts, 'A')# LLamo al parámetro de ipv4 del DNS
		 	 	ip=[] #Declaro un array vacío donde guardaré las ips
		 	 	for rdata in res:
		 	 		n = dns.reversename.from_address(rdata.address)
		 	 		try:
		 	 			res_inv = myresolver.query(n, 'PTR') #Llamo al puntero del nombre de dominio
		 	 			for rdata_inv in res_inv:
		 	 				ip += [(rdata.address, str(rdata_inv.target))] #array donde guardo ip y el nombre ns correspondinte
		 	 		except dns.resolver.NoAnswer:
		 	 			ip += [(rdata.address, "PTR: Sin respuesta "+str(n))]
		 	 		except dns.resolver.NXDOMAIN:
		 	 			ip += [(rdata.address, "PTR: Dominio NX "+str(n))]
		 	 	for i, j in ip:
		 	 		print "[+]El dominio " + hosts + " tiene la siguiente ip " + i + " correspondiente a " + j #imprimo en pantalla el resultado y si no el error correspondiente
		 	except dns.resolver.NoAnswer:
		 	 	print "[-] No se ha podido obtener ninguna información acerca del dominio" + hosts 
	ipv4(arr, myresolver)

#Esta función me sirve para capturar todos los ns disponibles de un host determinado;sigo la misma estructura realmente para todas las funciones
	def NSInfo(arr, myresolver):
		for hosts in arr:
			try:
				res = myresolver.query(hosts, 'NS')# LLamo al parámetro de name server del DNS
				ns = []
				for rdata in res:
					ns += [str(rdata.target)]
				for x in ns:
					print "[+]El dominio " + hosts + " tiene el siguiente name server: " + x #Imprimo en pantalla el resultado y si no el error correspondiente
			except dns.resolver.NXDOMAIN:
				print "[-]No se puede obtener ninguna información acerca de los NS del dominio: " + hosts #Error en caso de que no exista el dominio
			except dns.resolver.NoAnswer:
			    print "[-] No se ha recibido ninguna respuesta del dominio " + hosts
	NSInfo(arr, myresolver)

#Función que obtiene información acerca de los servidores de correo
	def mailInfo(arr, myresolver):
		for hosts in arr:
			try:
				res = myresolver.query(hosts, 'MX')# LLamo al parámetro de correos del DNS
				mx = []
				for rdata in res:
					mx += [str(rdata.exchange)]
				for x in mx:
					print "[+]El dominio " + hosts + " tiene el siguient servidor de correo: " + x #Imprimo en pantalla el resultado y si no el error correspondiente
			except dns.resolver.NoAnswer:
				print "MXs: No se puede obtener"
			except dns.resolver.NXDOMAIN:
				print "[-]No se puede obtener ninguna información acerca de los servidores de correo del dominio: " + hosts #Error en caso de que no exista el dominio
	mailInfo(arr, myresolver)

#Función que obtiene información acerca de los registros de inicio de actividad del dominio
	def soa(arr, myresolver):
		for hosts in arr:
			try:
				res = myresolver.query(hosts, 'SOA') #LLamo al parámetro necesario del DNS
				for rdata in res:
					print "[+]El dominio " + hosts + " tiene los siguientes registros de inicio de autoridad:" +  str(rdata.mname), str(rdata.rname) #Imprimo en pantalla el resultado y si no el error correspondiente
			except dns.resolver.NoAnswer:
				print "[-]No se pudo obtener ningun registro sobre los registros de inicio de actividad" #Error en caso de que no se reciba respuesta
			except dns.resolver.NXDOMAIN:
				print "[-]No se puede obtener ninguna información acerca de los registros de inicio de actividad del dominio: " + hosts #Error en caso de que no exista el dominio
	soa(arr, myresolver)

#"Inicializo la clase chee"   
if __name__ == '__chee__':
	chee(arr, myresolver)