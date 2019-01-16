.PHONY: test

test:
	cd ./test/ && python test.py

install:
	vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure --force
	vagrant plugin install vagrant-azure
	vagrant up --provider=azure
	fab install

update:
	fab actualizar

stop:
	fab parar

delete:
	fab borrar

start:
	fab despliegue
