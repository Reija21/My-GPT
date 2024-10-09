from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    # Crea un paquete ARP para descubrir dispositivos en la red
    arp_request = ARP(pdst=target_ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Envía el paquete y recibe las respuestas
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    devices = []
    for element in answered_list:
        devices.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})

    return devices


if __name__ == "__main__":
    target_ip = input("Introduce la puerta de enlace (ejemplo: 192.168.1.1/24): ")
    devices = scan_network(target_ip)

    print("Dispositivos encontrados en la red:")
    for device in devices:
        print(f"IP: {device['ip']} | MAC: {device['mac']}")
