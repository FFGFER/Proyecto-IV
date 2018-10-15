#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Videojuegos:
	
	def __init__(self):
		with open('videojuegos.json', 'r') as file:
			self.vg = json.load(file)
			
	def getVideojuego(self,idgame):
		
		try:
			idgame = abs(int(idgame))
			videojuego = self.vg["Videojuego"][idgame-1]["Nombre"]
		
		except:
			videojuego = False
		
		return videojuego