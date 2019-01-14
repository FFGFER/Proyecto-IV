[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.org/FFGFER/Proyecto-IV.svg?branch=master)](https://travis-ci.org/FFGFER/Proyecto-IV)
[![Heroku](https://heroku-badge.herokuapp.com/?app=tienda-vg)](https://tienda-vg.herokuapp.com/)

# Proyecto-IV - Tienda de videojuegos

Este proyecto estará enfocado a implementar un microservicio en la nube en una aplicación web enfocada a la compraventa de videojuegos. Enfocándonos principalmente en el microservicio de gestión del catálogo.

# Herramientas
* El lenguaje de programación que utilizaremos será Python, dado que nos será útil a la hora de utilizar el framework descrito en el siguiente punto.
* Nos apoyaremos en el framework Flask (estamos actualmente investigando sobre su uso en la asignatura Desarrollo de Aplicaciones para Internet, y esta es una oportunidad perfecta para su uso y profundización en el aprendizaje del mismo).
* Virtualizaremos el entorno de desarrollo con virtualenv.
* Cuando queramos realizar algún test, nos ayudaremos de la librería unittest y del programa pytest. Y a la hora de conseguir la integración continua utilizaremos Travis o Jenkins.
* Para la gestión de la base de datos de la que hará uso la aplicación se usará MariaDB.

# Instalación
Para instalar la aplicación y ejecutarla localmente deberemos ejecutar los siguientes comandos:
> git clone https://github.com/FFGFER/Proyecto-IV

> pip install -r requirements

> cd ./src && python3 tienda-vg

# Clases
* [videojuegos.py](https://github.com/FFGFER/Proyecto-IV/blob/master/src/videojuegos.py): Esta clase se encarga de gestionar el catálogo de videojuegos, puede devolvernos un array con todos los juegos que tengamos en nuestra base de datos (en este caso un archivo JSON de manera provisional), añadir y eliminar juegos de la base de datos. También puede extraer un juego en concreto dando como parámetro el ID del juego, y viceversa, se puede obtener el ID de un juego dando como parámetro el nombre del mismo.

# Integración continua
Este proyecto utiliza Travis-CI para la implementación de la integración continua.

Para testear la funcionalidad localmente hay que ejecutar los siguientes comandos, una vez tengamos los ficheros disponibles en nuestro almacenamiento local:
> pip install -r requirements.txt

> cd ./test/ && python test.py

[Documentación integración continua](https://ffgfer.github.io/Proyecto-IV/doc/integracion)

# Despliegue en PaaS
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Para que la aplicación funcione se ha elegido Heroku como PaaS en el que desplegar nuestro proyecto

El motivo principal por el que se ha elegido este PaaS por su facilidad de uso y por su carácter gratuito.

Despliegue [https://tienda-vg.herokuapp.com/](https://tienda-vg.herokuapp.com/status)

En [https://tienda-vg.herokuapp.com/](https://tienda-vg.herokuapp.com/) están las rutas y las intrucciones para probar el uso de la funcionalidad de la aplicación

[Documentación despliegue](https://ffgfer.github.io/Proyecto-IV/doc/despliegue)

## Contenedores

Contenedor: https://docker-tienda-vg.herokuapp.com/

Repositorio en Docker Hub: https://hub.docker.com/r/ffgfer/proyecto-iv/

Para obtener el contenedor basta con usar el comando que se indica en la propia página del repositorio: 
> docker pull ffgfer/proyecto-iv

Y para ejecutarlo nos basta con ejecutar: 
> docker run --rm -p 80:80 -it ffgfer/proyecto-iv

[Documentación contenedores](https://ffgfer.github.io/Proyecto-IV/doc/contenedores)

## Despliegue en la nube

Despliegue final: 13.73.145.25

Para desplegar en la nube debemos tener antes instalados en nuestra máquina local azure-cli, ansible, fabric y vagrant.

[Documentación despliegue en la nube](https://ffgfer.github.io/Proyecto-IV/doc/desplieguenube)


