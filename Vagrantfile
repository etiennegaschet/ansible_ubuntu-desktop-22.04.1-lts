# -*- mode: ruby -*-

$script = <<-SCRIPT

echo Starting provisioning...
echo Installing Desktop

export DEBIAN_FRONTEND=noninteractive

apt-get update

apt-get install -y software-properties-common
apt-get install -y ansible

ansible-pull -o -U https://github.com/etiennegaschet/ansible_ubuntu-desktop-22.04.1-lts.git

echo Finished provisioning...

SCRIPT

Vagrant.configure("2") do |config|

  config.vm.synced_folder "shared_data", "/vagrant_data"
  config.vm.box = "generic/ubuntu2204"
  config.vm.box_version = "4.1.14"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "4096"
     vb.cpus = 4
     vb.customize ['modifyvm', :id, '--accelerate2dvideo', 'on']
     vb.customize ['modifyvm', :id, '--accelerate3d', 'on']
     vb.customize ['modifyvm', :id, '--graphicscontroller', 'vboxsvga']
     vb.customize ['modifyvm', :id, '--clipboard', 'bidirectional']
     vb.customize ['modifyvm', :id, '--vram', '256']
  end

  config.vm.provision "shell", inline: $script

end
