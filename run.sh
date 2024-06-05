sudo apt-get update
sudo apt-get install ansible-core
ansible-playbook site.yml -K -i ansible/hosts.ini