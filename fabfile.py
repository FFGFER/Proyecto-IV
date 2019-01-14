from fabric.api import *

env.hosts = ['tienda-vg.westeurope.cloudapp.azure.com']
env.user = 'vagrant'

def hello():
	print("Hello world!")

def clonado():
	run("git clone https://github.com/FFGFER/Proyecto-IV")

def paquetes():
	with cd("Proyecto-IV"):
		run("sudo pip3 install -r requirements.txt")
def despliegue():
	with cd("Proyecto-IV"):
		run("sudo gunicorn tienda-vg:app --bind 0.0.0.0:80")
def parar():
	run("sudo pkill gunicorn")

def borrar():
	run("sudo rm -rf Proyecto-IV")

def actualizar():
	with cd("Proyecto-IV"):
		run("git pull")

def install():
	clonado()
	paquetes()
	despliegue()
