#!/usr/bin/env python3

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'admin',
    'password': 'cisco',
    }

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'admin',
    'password': 'cisco',
    }

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'admin',
    'password': 'cisco',
    }

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.74',
    'username': 'admin',
    'password': 'cisco',
    }

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'admin',
    'password': 'cisco',
    }


with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3]


for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
print (output)


with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s2, iosv_l2_s1]


for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
print (output)
