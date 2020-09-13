from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

'''
如果运行 
record, reminder = signal.deconvolve(res, sig)

就会报错 ValueError: BUG: filter coefficient a[0] == 0 not supported yet

也就是 signal.deconvolve() 的两个数组参数中，数组的第一个元素不能为0，也就是
sig[0] != 0
cv1[0] != 0

'''
sig = np.array([1, 0, 2, 3, 4, 5, 6, 7, 8, 9])
filtr = np.array([1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
res = signal.convolve(sig, filtr)
record, reminder = signal.deconvolve(res, sig)

plt.subplot(4, 1, 1)
plt.stem(sig)
plt.axis([0, 25, 0, 10])

plt.subplot(4, 1, 2)
plt.stem(filtr)
plt.axis([0, 25, 0, 5])

plt.subplot(4, 1, 3)
plt.stem(res)
plt.axis([0, 25, 0, 50])

plt.subplot(4, 1, 4)
plt.stem(record)
plt.axis([0, 25, 0, 5])


plt.show()

