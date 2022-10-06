# ansible_ubuntu-desktop-22.04.1-lts
Ansible config for Ubuntu Desktop (22.04.1-LTS) installation

## Ansible installation:
```bash
sudo apt update
sudo apt install ansible
```

## Ansible config deployment:
```bash
sudo ansible-pull -o -U https://github.com/etiennegaschet/ansible_ubuntu-desktop-22.04.1-lts.git
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