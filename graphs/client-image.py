import matplotlib.pyplot as plt
import numpy as np

N = 3
CPU = np.array([0.1838042816, 0.7334787415, 1.460498822])
LPM = np.array([0.04484839417, 0.1782684613, 0.3527386414])
TX = np.array([0.1194598389, 0.476189209, 0.9447739014])
RX = np.array([1.678172241, 6.673886536, 13.21756384])

CPUstd = np.array([0.000918334576, 0.001986588496, 0.002718812919])
LPMstd = np.array([0.001208184762, 0.001536797951, 0.003600616008])
TXstd = np.array([0.001205785423, 0.003752072953, 0.001893914224])
RXstd = np.array([0.0405420135, 0.05134885381, 0.1207698144])

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
plt.savefig("client-image.pdf")