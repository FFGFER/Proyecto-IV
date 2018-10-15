

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

# Proyecto-IV - Tienda de videojuegos

Este proyecto estará enfocado a implementar un microservicio en la nube en una aplicación web enfocada a la compraventa de videojuegos. Enfocándonos principalmente en el microservicio de gestión del catálogo.

# Herramientas
* El lenguaje de programación que utilizaremos será Python, dado que nos será útil a la hora de utilizar el framework descrito en el siguiente punto.
* Nos apoyaremos en el framework Flask (estamos actualmente investigando sobre su uso en la asignatura Desarrollo de Aplicaciones para Internet, y esta es una oportunidad perfecta para su uso y profundización en el aprendizaje del mismo).
* Virtualizaremos el entorno de desarrollo con virtualenv.
* Cuando queramos realizar algún test, nos ayudaremos de la librería unittest y del programa pytest. Y a la hora de conseguir la integración continua utilizaremos Travis o Jenkins.
* Para la gestión de la base de datos de la que hará uso la aplicación se usará MariaDB.

# Clases
videojuegos.py: Esta clase se encarga de gestionar el catálogo de videojuegos, aún está en fase de desarrollo pues solo está diseñado y codificado un método que devuelve los videojuegos que hay en nuestra base de datos (en este caso, provisional hecha con archivos JSON).
usuarios.py: Esta clase se encarga de gestionar los usuarios de nuestra aplicación, aún está en fase de desarrollo.

La aplicación aún no está disponible para su testeo.
