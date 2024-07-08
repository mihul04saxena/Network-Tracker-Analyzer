import pandas as pd
from scapy.all import rdpcap

# Load the pcap file
packets = rdpcap('r.pcap')

# Extract relevant data from packets
data = []
for packet in packets:
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        length = packet['IP'].len
        data.append([src_ip, dst_ip, protocol, length])

# Convert to a DataFrame
df = pd.DataFrame(data, columns=['Source IP', 'Destination IP', 'Protocol', 'Length'])

# Save to CSV
df.to_csv('network_data.csv', index=False)
