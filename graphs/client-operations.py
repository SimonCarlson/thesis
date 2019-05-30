import matplotlib.pyplot as plt
import numpy as np

N = 3
CPU = np.array([0.0006610290527, 0.003822756958, 0.0001319915771])
LPM = np.array([0.0001819207764, 0.0009533935547, 0])
TX = np.array([0.0005610351563, 0.002571972656, 0])
RX = np.array([0.006613342285, 0.035456604, 0.0002029418945])

CPUstd = np.array([0.00004632148074, 0.00004632148074, 0.0000003631596218])
LPMstd = np.array([0.0000716225263, 0.0001535282166, 0])
TXstd = np.array([0.00006111165061, 0.0004054953317, 0])
RXstd = np.array([0.002411339236, 0.00516864187, 0.0000006940594881])
ind = np.arange(N)
width = 0.35

# Plot bars
p1 = plt.bar(ind, CPU, width, fill=False, hatch="xxx", yerr=CPUstd,  ecolor="k", capsize=5, label="CPU")
p2 = plt.bar(ind, LPM, width, fill=False, hatch="|||", bottom=CPU, yerr=LPMstd,  ecolor="k", capsize=5, label="LPM")
p3 = plt.bar(ind, TX, width, fill=False, hatch="\\\\\\", bottom=CPU+LPM, yerr=TXstd,  ecolor="k", capsize=5, label="TX")
p4 = plt.bar(ind, RX, width, fill=False, hatch="///", bottom=CPU+LPM+TX, yerr=RXstd,  ecolor="k", capsize=5, label="RX")

# Labels
plt.ylabel("Joules")
plt.xticks(ind, ("Registration", "Manifest", "Decode and parse manifest"))

# Axis
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)
plt.gca().yaxis.grid(True, color="gray", linestyle="dashed")
plt.gca().set_axisbelow(True)

# Legend
handles, labels = plt.gca().get_legend_handles_labels()
plt.gca().legend(reversed(handles), reversed(labels), loc="upper left")

#plt.show()
plt.savefig("client-operations.pdf")