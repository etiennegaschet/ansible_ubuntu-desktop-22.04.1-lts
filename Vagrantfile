# -*- mode: ruby -*-

$script = <<-SCRIPT
echo Starting provisioning...
echo Installing Desktop

export DEBIAN_FRONTEND=noninteractive

apt-get install -y software-properties-common
apt-get install -y ansible

locale-gen en_US
locale-gen en_US.UTF-8

update-locale LANG=en_US.UTF-8
update-locale LANGUAGE=en_US.UTF-8

localectl set-x11-keymap fr

ansible-pull -o -U https://github.com/etiennegaschet/ansible_ubuntu-desktop-22.04.1-lts.git

echo Finished provisioning...
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.synced_folder "shared_data", "/vagrant_data"
  config.vm.box = "generic/ubuntu2204"
  config.vm.box_version = "4.1.14"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "4096"
     vb.cpus = 2
     vb.customize ['modifyvm', :id, '--graphicscontroller', 'vmsvga']
  end

  config.vm.provision "shell", inline: $script

end
