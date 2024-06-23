<h1 align="center">Offensive Kali Ansible Playbook</h1>

---

<p align="center"> This Ansible Playbook automates the setup of kali machines used for both external and internal penetration tests. The Ansible Roles included in this playbook automates the downloading and installalation of additional frameworks, packages, and offensive penetration testing and red-teaming utilities for a Kali Linux machine.
  <br>
  <b>This repository is a modified fork and contains my personal preferences</b>
</p>

## Table of Contents
+ [Description](#description)
+ [Getting Started](#getting_started)
+ [Roles](#roles)
+ [Issues](#issues)
+ [Authors](#authors)
+ [Acknowledgments](#acknowledgement)

## Description <a name = "description"></a>
This playbook contains multiple tasks embedded within the roles. The current roles included in this ansible playbook include the following:

- Common
  - Performs apt package updates, cleanup, and installation of common offensive packages
  - Installation of common offensive python packages
  - Installation of common git repos as well as setting up their package dependencies
  - Installation of binary only tools
  - Sets up basic zsh environment
  - Sets up and install python models and packages
  - Sets up burpsuite and installs certificate into firefox
  - Sets up firefox and installs extensions
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

## Issues <a name = "issues"></a>
- the automatic burp certificate is not working
- ngrok

## Authors <a name = "authors"></a>
- [@AdamZvara](https://github.com/AdamZvara)

## Acknowledgements <a name = "acknowledgement"></a>
- [@hackedbyagirl](https://github.com/kylelobo) (original ansible script)
- [@ippsec.rocks](https://github.com/IppSec) (burpsuite, firefox)
- [@cisagov - ansible-role-kali](https://github.com/cisagov/ansible-role-kali)
