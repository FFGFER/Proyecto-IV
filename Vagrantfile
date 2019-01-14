Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  # Configuramos el path de las claves para posterior acceso con ssh
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  config.vm.provider :azure do |azure, override|

    # Las siguientes variables las configuramos mediante las variables de entorno
    # las obtenemos mediante la ejecución de los comandos az ad sp create-for-rbac
    # y az account list --query "[?isDefault].id" -o tsv 
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Indicamos que nombre queremos que tenga la MV en azure
    azure.vm_name = "tienda-vg"
    # Abrimos el puerto 80 para tener acceso al servidor mediante el navegador
    azure.tcp_endpoints = "80"
    # Señalamos a azure que queremos que la localización de la mv sea en el Oeste de EUropa
    azure.location = "westeurope"
  end

  # Configuramos el path de hosts y el archivo YAML para provisionar nuestra máquina
  # al iniciarla directamente.
  config.vm.provision "ansible" do |ansible|
    ansible.inventory_path = "/etc/ansible/hosts"
    ansible.limit = "all"
    ansible.playbook = "provision/provision.yml"
  end

end
