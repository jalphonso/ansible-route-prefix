This playbook demonstrates how to install or
update a route prefix list on a Junos device.

To run, update credentials in group_vars/all.yml,
list of hosts in site.yml, and execute:
```
ansible-playbook -i hosts site.yml -vv
```

A diff of the config will be saved for each
device with a timestamp.
