<h1 align="center">Offensive Kali Ansible Playbook</h1>

---

## Description <a name = "description"></a>
This playbook contains multiple tasks embedded within the roles. The current roles included in this ansible playbook include the following:

- Common
  - Performs apt package updates, cleanup, and installation of common offensive packages
  - Installation of common offensive python packages
  - Installation of common git repos as well as setting up their package dependencies
  - Installation of binary only tools
  - Sets up basic zsh environment
  - Sets up and install python models and packages
- External
  - Not used - maybe in future for external pentesting tools
- Internal
  - Not used - maybe in future for internal pentesting tools

## Getting Started <a name = "getting_started"></a>
Currently, only *common* role is being installed
on a local kali host machine (for me it's a virtual machine guest inside Windows).

To run the playbook, you can do `./run.sh`, which
  - runs `apt-get update` to be able to install ansible-playbook
  - installs `ansible-core` to run ansible-playbook
  - finally runs the playbook on localhost with `ansible-playbook -i ansible/hosts.ini site.yml -K`

## Roles <a name = "roles"></a>
To decide which roles you would like to do, edit the `site.yml` file (by default only `common` role is used). Each
role follows the basic ansible structure
- files - contains any files used in tasks (usually helper scripts or configuration)
- tasks - the actual tasks to be performed - must contain `main.yml` which can reference other tasks
- vars - local variables defined for the tasks (you might want to check them out if you want to adjust install directories, packages etc...)

## Manual Configuration <a name = "issues"></a>

Some manual configuration is still needed:

- remeber to set correct resources to VM - 4GB RAM and 2 cores is usually enough
- set port forwarding rules
  - I usually tunnel SSH through host port 3022
  - if IDA is needed, tunnel it through host port 3023 and guest port 23946
  - burp through port 3024
- my current setup for web challs is running browser in host and tunneling it to the VM
  - use foxyproxy in the browser (I use brave) and set it up to forward to localhost port 3024
  - add certificate manually, it does not take long and is a one time action

