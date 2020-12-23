from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 10)
value = np.sin(2 * np.pi * t)
plt.plot(t, value, 'b^', ms=6, label='real value')

f1 = interp1d(t, value)  # 產生線性插值函數
x = np.linspace(0, 10, 50)  # 將間隔細分為50個區段
y = f1(x)  # 利用線性插值函數產生50個插值
plt.plot(x, y, "ro", label='linear interplot')


f1 = interp1d(t, value)  # 產生線性插值函數
x = np.linspace(0, 10, 50)  # 將間隔細分為50個區段
# y = interp1d(x)  # 利用線性插值函數產生50個插值
# plt.plot(x, y, label='linear interplot')


x = np.linspace(0, 10, 200)
f3 = interp1d(t, value, kind='cubic')  # 取得三次插值法函數
y = f3(x)  # 取得三次插值的值
plt.plot(x, y, label='cubic interpolate')
plt.show()

# import numpy as np
# from scipy.interpolate import interp1d

# x = np.linspace(0, 10, num=11, endpoint=True)
# y = np.cos(-x**2/9.0)
# f = interp1d(x, y)
# f2 = interp1d(x, y, kind='cubic')

# xnew = np.linspace(0, 10, num=41, endpoint=True)
# import matplotlib.pyplot as plt
# plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
# plt.legend(['data', 'linear', 'cubic'], loc='best')
# plt.show()