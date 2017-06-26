#!/usr/bin/env python

from netaddr import IPNetwork
from netaddr import cidr_merge
import sys
import yaml

prefixes = []
input_file = 'prefixlist.txt'
yaml_file = '../../../group_vars/all.yml'

#read prefixlist txt file, validate input, convert to consistent format
try:
    with open(input_file, 'r') as fin:
        for line in fin:
            line = line.strip()
            ip = IPNetwork(line)
            #save network cidr; corrects non network input
            prefixes.append(ip.cidr)
except Exception as exc:
    print("error opening txt file for read")
    print(exc)

#sort and summarize
prefixes = cidr_merge(prefixes)
#convert List of IPNetwork objects to list of strings
prefixes = [str(prefix) for prefix in prefixes]

#load original all.yml file; read/write combo causes unexpected behavior
#therefore we separate those operations out
try:
    with open(yaml_file, 'r') as allyaml:
        try:
            myyaml = yaml.load(allyaml)
            if myyaml['prefixes'] == prefixes:
                print("prefixlist yaml file is current with the txt file")
                sys.exit()
            myyaml['prefixes'] = prefixes
        except yaml.YAMLError as exc:
            print("YAML load error")
            print(exc)
except Exception as exc:
    print("error opening yaml file for read")
    print(exc)

#write updated yaml data back to file
try:
    with open(yaml_file, 'w') as allyaml:
        try:
            yaml.dump(myyaml, allyaml, default_flow_style=False)
        except yaml.YAMLError as exc:
            print("YAML dump error")
            print(exc)
except Exception as exc:
    print("error opening yaml file for write")
    print(exc)
