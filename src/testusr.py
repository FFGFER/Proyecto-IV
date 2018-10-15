#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import usuarios

class Test(unittest.TestCase):

	test = usuarios.Usuarios()

	def testUusarios(self):
		self.assertEqual(self.test.getUsuario("cad"),False,"El ID del usuario debe ser entero")
		self.assertEqual(self.test.getUsuario(1),str('Fernando Flores'),"El ID del usuario es correcto y es devuelto")

if __name__ == '__main__':
    unittest.main()          