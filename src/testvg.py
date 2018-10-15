#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import videojuegos

class Test(unittest.TestCase):

	test = videojuegos.Videojuegos()

	def testVideojuegos(self):
		self.assertEqual(self.test.getVideojuego("cad"),False,"El ID del videojuego debe ser entero")
		self.assertEqual(self.test.getVideojuego(1),str('BattleRoyale'),"El ID del videojuego es correcto y es devuelto")


if __name__ == '__main__':
    unittest.main()                                                  
