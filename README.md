# ansible_ubuntu-desktop-22.04.1-lts
Ansible config for Ubuntu Desktop (22.04.1-LTS) installation

## Ansible installation:
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

## Ansible config deployment:
```bash
ansible-pull -o -U https://github.com/jlacroix82/ansible_pull_tutorial.git
```
### flags:
```bash
-o, --only-if-changed
```
only run the playbook if the repository has been updated

```bash
-U <URL>, --url <URL>
```
URL of the playbook repository