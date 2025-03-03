sudo apt-get update
sudo apt-get install ansible-core

set -m
touch /home/kali/.ansible_debug && tail -f /home/kali/.ansible_debug & # Set up logging file
ansible-playbook site.yml -K -i ansible/hosts.ini -v
kill %1 # stop logging process

rm -rf /home/kali/.ansible_debug # comment to keep the log file for debugging purposes