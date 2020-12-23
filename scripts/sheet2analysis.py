import matplotlib.pyplot as plt
import numpy as np
import csv

ts = []
setting_flow_rate = []

tm = []
machine_flow_rate = []

with open('./data/sheet2.csv', newline='') as csvfile:

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

    plt.plot(ts, setting_flow_rate)
    plt.plot(tm, machine_flow_rate)
    plt.xticks(np.linspace(0, 5 , num=11, endpoint=True))
    plt.yticks(np.linspace(0, 50, num=11, endpoint=True))
    plt.title('sheet2')
    plt.grid()
    plt.show()
