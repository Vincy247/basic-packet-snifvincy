from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def process_packet(packet):
    if packet.haslayer(IP):

        print("=" * 60)

        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")

        else:
            print("Protocol Number:", packet[IP].proto)

        if packet.haslayer("Raw"):
            payload = bytes(packet["Raw"]).decode(errors="ignore")
            print("Payload:")
            print(payload[:200])

sniff(prn=process_packet, store=False)

