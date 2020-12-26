from scipy import signal
from scipy.signal import lsim2
from scipy.interpolate import interp1d
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

# origin signal.
# plt.plot(ts, setting_flow_rate, 'b.-', label='setting flow rate')
# resample signal.
f = interp1d(ts, setting_flow_rate)
ts = tm
setting_flow_rate = f(tm)
plt.plot(ts, setting_flow_rate, 'k.-', label='setting flow rate')

wn = 33
zeta = 0.0087
tout, yout, xout = lsim2(([1, wn*wn], [1, zeta*wn*wn, wn*wn]), U=setting_flow_rate[:-25], T=ts[:-25])

plt.plot(tm, machine_flow_rate, 'r.-', label='machine flow rate')
plt.plot(tout, yout, 'b.-', label='simulation')

plt.xticks(np.linspace(0, 5, num=11, endpoint=True))
plt.yticks(np.linspace(0, 50, num=11, endpoint=True))
plt.title('sheet3')
plt.legend()
plt.grid()
plt.savefig('./img/data_restruct.png')
plt.show()
