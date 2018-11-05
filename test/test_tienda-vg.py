# -*- coding: utf-8 -*-
import unittest, json, requests
from requests import *

url = 'https://tienda-vg.herokuapp.com/'

class testTiendaVG(unittest.TestCase):
    def test_root(self):
        response = requests.get(url)
        self.assertEqual(response.json()['status'],'Ok', "Estado correcto")

    def test_vgs(self):
        response = requests.get(url+'/videojuegos')
        self.assertEqual(response.json()[0],"BattleRoyale", "Correcto")
        self.assertEqual(response.json()[1], "MOBA", "Nombre correcto")

if __name__ == '__main__':
	unittest.main()
