
# Basic Packet Sniffer

A Python packet sniffing tool built using Scapy to monitor and display real-time network traffic (IP & ICMP protocols).

## Usage / Command Lines
To run the sniffer with root permissions:
```bash
sudo python3 sniffer.py

Source IP: 192.168.6.128
Destination IP: 172.217.22.46
Protocol: ICMP
Payload:
[nj<
    ▒▒!"#$%&'()*+,-./01234567
============================================================
Source IP: 172.217.22.46
Destination IP: 192.168.6.128
Protocol: ICMP
Payload:
[nj<
    ▒▒!"#$%&'()*+,-./01234567
============================================================
Source IP: 192.168.6.128
Destination IP: 172.217.22.46
Protocol: ICMP
Payload:
[nj-C
     ▒▒!"#$%&'()*+,-./01234567
============================================================
Source IP: 172.217.22.46
Destination IP: 192.168.6.128
Protocol: ICMP
Payload:
[nj-C
     ▒▒!"#$%&'()*+,-./01234567

