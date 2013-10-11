import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming
from scipy.fftpack import fft, fftshift

plt.figure(1)
M= 64
N = 256
x = np.cos(2*np.pi*3/M*np.arange(M)) * np.hanning(M)

plt.subplot(3,1,1)
plt.plot(x, 'b')
plt.axis([0,M-1,-1,1])
plt.title('x')


mX = np.abs(fftshift(fft(x, N)))
plt.subplot(3,1,2)
plt.plot(np.arange(-N/2,N/2,1), mX, 'r')
plt.axis([-N/2,N/2,0,max(mX)])
plt.title('abs(X)')

mX = 20 * np.log10(mX)
plt.subplot(3,1,3)
plt.plot(np.arange(-N/2,N/2,1), mX, 'r')
plt.axis([-N/2,N/2,-50,max(mX)])
plt.title('20*log10(abs(X))')

plt.show()