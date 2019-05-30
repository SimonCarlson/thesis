import matplotlib.pyplot as plt
import numpy as np


N = 3
sent = (16000, 64000, 128000)
actualData = (12000, 48000, 96000)

fig, ax = plt.subplots()

ind = np.arange(N)    
width = 0.35         
# Plot bars
p1 = ax.bar(ind, sent, width, fill=False, hatch="///", bottom=0, label="Bytes sent")
p2 = ax.bar(ind + width, actualData, width, fill=False, hatch="\\\\\\", bottom=0, label="Actual data")

# Labels
plt.ylabel("Bytes")
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(("500 blocks", "2000 blocks", "4000 blocks"))

# Axis
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)
plt.gca().yaxis.grid(True, color="gray", linestyle="dashed")
plt.gca().set_axisbelow(True)

# Legend
handles, labels = plt.gca().get_legend_handles_labels()
#plt.gca().legend(reversed(handles), reversed(labels), loc="upper left")
plt.gca().legend(loc="upper left")

#plt.show()
plt.savefig("overhead.pdf")