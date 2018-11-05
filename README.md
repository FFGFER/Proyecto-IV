

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.org/FFGFER/Proyecto-IV.svg?branch=master)](https://travis-ci.org/FFGFER/Proyecto-IV)

# Proyecto-IV - Tienda de videojuegos

Este proyecto estará enfocado a implementar un microservicio en la nube en una aplicación web enfocada a la compraventa de videojuegos. Enfocándonos principalmente en el microservicio de gestión del catálogo.

# Herramientas
* El lenguaje de programación que utilizaremos será Python, dado que nos será útil a la hora de utilizar el framework descrito en el siguiente punto.
* Nos apoyaremos en el framework Flask (estamos actualmente investigando sobre su uso en la asignatura Desarrollo de Aplicaciones para Internet, y esta es una oportunidad perfecta para su uso y profundización en el aprendizaje del mismo).
* Virtualizaremos el entorno de desarrollo con virtualenv.
* Cuando queramos realizar algún test, nos ayudaremos de la librería unittest y del programa pytest. Y a la hora de conseguir la integración continua utilizaremos Travis o Jenkins.
* Para la gestión de la base de datos de la que hará uso la aplicación se usará MariaDB.

# Documentación
Toda la documentación relativa al proyecto se encuentra aquí: [https://ffgfer.github.io/Proyecto-IV/doc](https://ffgfer.github.io/Proyecto-IV/doc)

# Clases
* [videojuegos.py](https://github.com/FFGFER/Proyecto-IV/blob/master/src/videojuegos.py): Esta clase se encarga de gestionar el catálogo de videojuegos, aún está en fase de desarrollo pues solo está diseñado y codificado un método que devuelve los videojuegos que hay en nuestra base de datos (en este caso, provisional hecha con archivos JSON).
* [usuarios.py](https://github.com/FFGFER/Proyecto-IV/blob/master/src/usuarios.py): Esta clase se encarga de gestionar los usuarios de nuestra aplicación, aún está en fase de desarrollo.

La aplicación aún no está disponible para su testeo.
