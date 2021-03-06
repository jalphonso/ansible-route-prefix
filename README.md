This playbook demonstrates how to install or
update a route prefix list on a Junos device.

Create dirs

```
mkdir configs output
```

Example Run
```
(.venv) ansible-route-prefix % ansible-playbook -e ansible_python_interpreter=$(which python) -i hosts update_prefix_list.pb.yml

PLAY [routers] ******************************************************************************************************************************************************************************************************************************

TASK [Validate, Summarize, Sort IP Prefixes] ************************************************************************************************************************************************************************************************
ok: [172.31.31.30]

TASK [save prefixes to var] *****************************************************************************************************************************************************************************************************************
ok: [172.31.31.30]

TASK [Build config snippet from template] ***************************************************************************************************************************************************************************************************
changed: [172.31.31.30]

TASK [Deploy Junos config to device] ********************************************************************************************************************************************************************************************************
changed: [172.31.31.30]

PLAY RECAP **********************************************************************************************************************************************************************************************************************************
172.31.31.30               : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

(.venv) ansible-route-prefix % more configs/172.31.31.30-route_prefix_snipp.conf
policy-options {
    replace:
    prefix-list accept-prefixes {
        1.1.1.0/29;
        2.2.2.0/30;
        3.3.3.0/24;
        5.5.5.0/24;
        6.6.6.0/28;
        8.8.8.0/30;
        8.8.8.8/32;
        9.9.8.0/23;
        10.0.0.0/8;
        172.16.0.0/12;
        192.168.0.0/16;
    }
}
(.venv) ansible-route-prefix % more output/172.31.31.30.diff

[edit]
+  policy-options {
+      prefix-list accept-prefixes {
+          1.1.1.0/29;
+          2.2.2.0/30;
+          3.3.3.0/24;
+          5.5.5.0/24;
+          6.6.6.0/28;
+          8.8.8.0/30;
+          8.8.8.8/32;
+          9.9.8.0/23;
+          10.0.0.0/8;
+          172.16.0.0/12;
+          192.168.0.0/16;
+      }
+  }
```

