#!/usr/bin/env python
from __future__ import print_function
import sys
from util import get_url
import re
import csv

report_fields = ["Hostname", "IP Address", "Utilization in %", "Total ports", "Total up"]

def list_network_devices():
    return get_url("network-device")['response']

def get_interfaces(id):
   return get_url("interface/network-device/%s" % id)

def print_info(interfaces):
    total_up = 0
    total_ports = 0
    for interface in interfaces['response']:
        if interface['interfaceType'] == "Physical":
            total_ports +=1
            if interface['status'] == "up":
                total_up+=1
        if total_ports == 0:
            utilization = 0
        else:
            utilization = (total_up * 100) / total_ports
    return utilization,total_ports,total_up
        writer = csv.DictWriter(f, fieldnames=report_fields)
if __name__ == "__main__":
    with open('interface_utilization.csv', "w") as f:
        writer = csv.DictWriter(f,report_fields)
        writer.writeheader()
        response = list_network_devices()
        for device in response:
            dev_id = device['id']
            mgmt_ip = device['managementIpAddress']
            hostname = device['hostname']
            interfaces = get_interfaces(dev_id)
            utilization, total_ports, total_up = print_info(interfaces)
            print(hostname, mgmt_ip, "Utilization:{utilization}, Total ports:{total_ports}, Total up:{total_up}".
            format(total_ports=total_ports,
                total_up=total_up,
                utilization='{}%'.format(utilization)))
            writer.writerow({"Hostname": hostname,
                            "IP Address": mgmt_ip,
                            "Utilization in %": '{}%'.format(utilization),
                            "Total ports": total_ports,
                            "Total up": total_up})
                            "Total ports": total_ports,
                            "Total up": total_up})




