import scapy.all as scapy

def scan(ip):
    #scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        clients_dic = {"IP":element[1].psrc , "MAC":element[1].hwsrc}
        clients_list.append(clients_dic)
    return clients_list

def print_result(result_list):
    print("IP\t\tMAC ADDRESS\n------------------------------------")
    for client in result_list:
        print(client["IP"] + "\t" + client["MAC"])



scan_result = scan("10.0.2.1/24")
print_result(scan_result)