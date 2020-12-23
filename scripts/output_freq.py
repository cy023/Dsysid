import matplotlib.pyplot as plt
import numpy as np
import csv

ts = []
setting_flow_rate = []

tm = []
machine_flow_rate = []

with open('./data/sheet3.csv', newline='') as csvfile:

    rows = csv.reader(csvfile)

    for row in rows:
        if row[0].isnumeric():
            ts.append(float(row[1]))
            setting_flow_rate.append(float(row[2]))
            tm.append(float(row[5]))
            machine_flow_rate.append(float(row[6]))
        elif row[4].isnumeric():
            tm.append(float(row[5]))
            machine_flow_rate.append(float(row[6]))

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 7))

axes[0].set_title("Signal")
axes[0].plot(tm, machine_flow_rate, color='C0')
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Amplitude")

axes[1].set_title("Magnitude Spectrum")
axes[1].magnitude_spectrum(machine_flow_rate, Fs=1, color='C1')

axes[2].set_title("Phase Spectrum")
axes[2].phase_spectrum(machine_flow_rate, Fs=1, color='C2')

fig.tight_layout()
plt.savefig('./img/out_freq.png')
plt.show()