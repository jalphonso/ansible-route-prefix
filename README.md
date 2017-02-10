# ansible-route-prefix
push route prefix changes to devices via ansible

Tested using Ansible 2.2.1

junos_config is part of Ansible core
junos_rollback is part of Ansible Galaxy

The rollback1.yml is unrelated but helpful for 
testing.

my /etc/ansible/hosts file contained the following:
```
[vmxs]
w3-vmx2
w3-vmx3
```

These hosts' connection details are in my .ssh/config
and key based authentication was used.


To use simply update your host/username info and then
execute:
```
ansible-playbook deploy_changes.yml
```
and to rollback:
```
ansible-playbook rollback1.yml
```

A backup of the config will be saved in the backup
directory for each device but only the most recent.
