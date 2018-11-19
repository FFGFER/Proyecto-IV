# Despliegue
Para desplegar nuestra aplicación en Heroku hemos seguido los siguientes pasos:

## Paso 1
Nos registramos en Heroku a través de su página web: [https://www.heroku.com/](https://www.heroku.com/)

## Paso 2
Iniciamos sesión en Heroku a través de la terminal:
> heroku login

![Inicio de sesión](img/2.jpg)

## Paso 3
Creamos la aplicación en heroku mediante el comando siguiente:
> heroku apps:create --region eu tienda-vg

![App en Heroku](img/9.jpg)

## Paso 4
Añadimos al requirements.txt la instalación de gunicorn, que es un servidor web compatible con el framework de aplicaciones webs Flask.

## Paso 5
Creamos el archivo [Procfile](https://github.com/FFGFER/Proyecto-IV/Procfile), con este archivo, y con su contenido (web: cd src && gunicorn tienda-vg:app) indicamos a Heroku que ese comando es el que debe ser utilizado para iniciar el servidor web. 

## Paso 6
Conectamos la aplicación de Heroku con nuestro repositorio de GitHub, esto se puede hacer en la sección Deploy del menú de la app en la página web de Heroku:
![Conexión con Github](img/7.jpg)

## Paso 7
Activamos el despliegue automático, así con cada push que hagamos a nuestro repositorio, se actualizará la build del despliegue (en caso de que nuestro commit pase los tests que tengamos configurados en nuestra integración continua):
![Deploys automáticos](img/10.jpg)
