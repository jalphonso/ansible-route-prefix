#!/usr/bin/env python
from ansible.plugins.action import ActionBase

from netaddr import IPNetwork
from netaddr import cidr_merge


class ActionModule(ActionBase):

    def run (self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        result['changed'] = False
        result['failed'] = False

        prefixes = []
        input_file = task_vars['prefix_file']

        #read prefixlist txt file, validate input, convert to consistent format
        try:
            with open(input_file, 'r') as fin:
                for line in fin:
                    line = line.strip()
                    ip = IPNetwork(line)
                    #save network cidr; corrects non network input
                    prefixes.append(ip.cidr)
        except Exception as exc:
            result['failed'] = True
            result['msg'] = "error opening txt file for read"
            return result

        #sort and summarize
        prefixes = cidr_merge(prefixes)
        #convert List of IPNetwork objects to list of strings
        prefixes = [str(prefix) for prefix in prefixes]

        result['prefixes'] = prefixes
        result['msg'] = "prefixes have been processed and loaded"
        return result
