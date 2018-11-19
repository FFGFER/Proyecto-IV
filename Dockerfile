FROM python:3.6-alpine

MAINTAINER Fernando Flores <ffgfer@correo.ugr.es>

WORKDIR Proyecto-IV/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR src/

CMD gunicorn tienda-vg:app --bind 0.0.0.0:80 
