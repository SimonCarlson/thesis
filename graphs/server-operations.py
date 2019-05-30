import matplotlib.pyplot as plt
import numpy as np

N = 2
CPU = np.array([0.000744619751, 0.004031832886])
LPM = np.array([0, 0.000823493042])
TX = np.array([0, 0.002816088867])
RX = np.array([0.001145751953, 0.03130560303])

CPUstd = np.array([0.00002335727481, 0.00004097692291])
LPMstd = np.array([0, 0.0001278287866])
TXstd = np.array([0, 0.000003716510666])
RXstd = np.array([0.00003626876241, 0.004300987928])

ind = np.arange(N)
width = 0.35

# Plot bars
p1 = plt.bar(ind, CPU, width, fill=False, hatch="xxx", yerr=CPUstd,  ecolor="k", capsize=5, label="CPU")
p2 = plt.bar(ind, LPM, width, fill=False, hatch="|||", bottom=CPU, yerr=LPMstd,  ecolor="k", capsize=5, label="LPM")
p3 = plt.bar(ind, TX, width, fill=False, hatch="\\\\\\", bottom=CPU+LPM, yerr=TXstd,  ecolor="k", capsize=5, label="TX")
p4 = plt.bar(ind, RX, width, fill=False, hatch="///", bottom=CPU+LPM+TX, yerr=RXstd,  ecolor="k", capsize=5, label="RX")

# Labels
plt.ylabel("Joules")
plt.xticks(ind, ("Registration", "Manifest"))

# Axis
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)
plt.gca().yaxis.grid(True, color="gray", linestyle="dashed")
plt.gca().set_axisbelow(True)

# Legend
handles, labels = plt.gca().get_legend_handles_labels()
plt.gca().legend(reversed(handles), reversed(labels), loc="upper left")

#plt.show()
plt.savefig("server-operations.pdf")