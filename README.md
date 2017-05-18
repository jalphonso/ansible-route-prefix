# ansible-route-prefix
push route prefix changes to devices via ansible

Tested using Ansible 2.3

To use simply update your host/username info and then
execute:
```
ansible-route-prefixible-playbook -i hosts deploy_changes.yml -vv
```

A diff of the config will be saved
