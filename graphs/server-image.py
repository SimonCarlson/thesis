import matplotlib.pyplot as plt
import numpy as np

N = 3
CPU = np.array([0.2038853302, 0.8209893951, 1.646202045])
LPM = np.array([0.04379889221, 0.1741164697, 0.3440461322])
TX = np.array([0.142171875, 0.5692629639, 1.137285791])
RX = np.array([1.654991089, 6.592557495, 13.05308423])

CPUstd = np.array([0.0004936030601, 0.001653833922, 0.002960744548])
LPMstd = np.array([0.001204101027, 0.001563795897, 0.003574288841])
TXstd = np.array([0.0003228393995, 0.000868800205, 0.0009382682704])
RXstd = np.array([0.04004990673, 0.05281899214, 0.1207197374])

ind = np.arange(N)
width = 0.35

# Plot bars
p1 = plt.bar(ind, CPU, width, fill=False, hatch="xxx", yerr=CPUstd,  ecolor="k", capsize=5, label="CPU")
p2 = plt.bar(ind, LPM, width, fill=False, hatch="|||", bottom=CPU, yerr=LPMstd,  ecolor="k", capsize=5, label="LPM")
p3 = plt.bar(ind, TX, width, fill=False, hatch="\\\\\\", bottom=CPU+LPM, yerr=TXstd,  ecolor="k", capsize=5, label="TX")
p4 = plt.bar(ind, RX, width, fill=False, hatch="///", bottom=CPU+LPM+TX, yerr=RXstd,  ecolor="k", capsize=5, label="RX")

# Labels
plt.ylabel("Joules")
plt.xticks(ind, ("500 blocks", "2000 blocks", "4000 blocks"))

# Axis
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)
plt.gca().yaxis.grid(True, color="gray", linestyle="dashed")
plt.gca().set_axisbelow(True)

# Legend
handles, labels = plt.gca().get_legend_handles_labels()
plt.gca().legend(reversed(handles), reversed(labels), loc="upper left")

#plt.show()
plt.savefig("server-image.pdf")