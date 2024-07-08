import pandas as pd
import matplotlib.pyplot as plt

# Load the network data
df = pd.read_csv('network_data.csv')

# Example visualization: Number of packets per protocol
protocol_counts = df['Protocol'].value_counts()

plt.figure(figsize=(10, 6))
ax = protocol_counts.plot(kind='bar')
plt.xlabel('Protocol')
plt.ylabel('Number of Packets')
plt.title('Number of Packets per Protocol')

# Rotate the x-axis labels vertically
ax.set_xticklabels(protocol_counts.index, rotation=0, ha='right')


plt.show()