from scapy.all import sniff, IP, TCP, UDP

def analyze_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"
        print(f"[{proto}] {src_ip} -> {dst_ip}")

        if packet.haslayer(TCP):
            print(f"    Port: {packet[TCP].sport} -> {packet[TCP].dport}")

# Capture 20 packets on your default interface
sniff(prn=analyze_packet, count=20)
