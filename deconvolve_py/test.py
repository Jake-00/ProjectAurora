import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve, deconvolve

x = np.linspace(1, 20, 20)
t = np.linspace(1, 10, 11, endpoint=False)[np.newaxis]
d = np.ones((1, 14), dtype=np.int16)
cv1 = fftconvolve(t, d, 'full')
cv2 = fftconvolve(t, d, 'same')
cv3 = fftconvolve(t, d, 'valid')

# plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
# plt.xlim(0.5, 4.5)
# plt.show()
# print(t[0][3])


plt.subplot(4, 1, 1)
plt.stem(t[0])
plt.axis([0, 25, 0, 10])

plt.subplot(4, 1, 2)
plt.stem(d[0])
plt.axis([0, 25, 0, 10])

plt.subplot(4, 1, 3)
plt.stem(cv1[0])
plt.axis([0, 25, 0, 60])

print(cv1)

# t_bak = np.zeros((1, len(t[0])))
# for i in range(len(t[0])):
#     t_bak[0][i] = t[0][i]
#
# cv1_bak = np.zeros((1, len(cv1[0])))
# for i in range(len(cv1[0])):
#     cv1_bak[0][i] = cv1[0][i]
t_bak = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
cv1_bak = [1., 2.81818182, 5.45454545, 8.90909091, 13.18181818, 18.27272727,
           24.18181818, 30.90909091, 38.45454545, 46.81818182, 56., 56.,
           56., 56., 55., 53.18181818, 50.54545455, 47.09090909, 42.81818182,
           37.72727273, 31.81818182, 25.09090909, 17.54545455, 9.18181818]

cv4, r = deconvolve(cv1_bak, t_bak)
plt.subplot(4, 1, 4)
plt.stem(cv4)
plt.axis([0, 25, 0, 5])

plt.show()
