#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Usuarios:
	
	def __init__(self):
		with open('usuarios.json', 'r') as file:
			self.usr = json.load(file)
			
	def getUsuario(self,idusr):
		
		try:
			idusr = abs(int(idusr))
			usuario = self.usr["Usuario"][idusr-1]["Nombre"]
		
		except:
			usuario = False
		
		return usuario