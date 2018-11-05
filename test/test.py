#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../src/')
import unittest
import videojuegos

class Test(unittest.TestCase):

	test = videojuegos.Videojuegos()

	def testVideojuegos(self):
		self.assertEqual(self.test.getVideojuego("cad"),False,"El ID del videojuego debe ser entero")
		self.assertEqual(self.test.getVideojuego(1),str('BattleRoyale'),"El ID del videojuego es correcto y es devuelto")
		
		self.assertEqual(self.test.getVideojuegos(),[str('BattleRoyale'), str('MOBA')],"Se devuelve el vector de juegos correctamente")
		
		self.assertEqual(self.test.aniadeVideojuego(-1),False,"El nombre del videojuego debe ser una cadena")
		self.assertEqual(self.test.aniadeVideojuego("cadena"),True,"Se ha añadido el juego correctamente")
		
		self.assertEqual(self.test.encuentraVideojuego(-1),False,"El nombre del videojuego debe ser una cadena")
		self.assertEqual(self.test.encuentraVideojuego("prueba"),False,"No se ha encontrado ningún juego con ese nombre")
		self.assertEqual(self.test.encuentraVideojuego("BattleRoyale"),0,"Se ha encontrado el ID del juego")
		
		self.assertEqual(self.test.borraVideojuego(-1),False,"El nombre del videojuego debe ser una cadena")
		self.assertEqual(self.test.borraVideojuego("cadena"),True,"Se ha borrado el juego correctamente")
		
if __name__ == '__main__':
    unittest.main()                                                  
