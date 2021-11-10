import numpy as np 
import matplotlib.pyplot as plt
import scipy
from scipy.signal import filtfilt
from scipy import stats
import pandas as pd

df = pd.read_csv (r'C:/Users/user999/Desktop/55.csv')
print (df)

# Goals:
# 1 - Compute FFT using Numpy "fft" function
# 2 - Plot the frequency spectrum using matplotlib

# Construct a time signal
#Fs = 2000 # sampling frequency
def sleep(haha,col):
    Fs=len(df.timestamps)/540 #all bci recorded is of 1 min
    tstep = 1 / Fs # sample time interval(inverse of frequency)
#f0 = 100 # signal frequency

#N = int(10 * Fs / f0) # number of samples
    N=len(df.timestamps)
    t = np.linspace(0, (N-1)*tstep, N) # time steps
    fstep = Fs / N # frequency interval
    f = np.linspace(0, (N-1)*fstep, N) # frequency steps

#y = 1 * np.sin(2 * np.pi * f0 * t) # sine wave
#af7= df.loc[:,'AF7']
    af7= df.loc[:,haha]
    AF7 = af7.values
    y=AF7 #cmi...?
#plt.plot(t,y)
    X = np.fft.rfft(y)
    X_mag = np.abs(X)

    f_plot = np.fft.rfftfreq(N,1/Fs)

    plt.plot(f_plot, X_mag,col)

sleep('AF7','r')
sleep('AF8','g')
sleep('TP9','b')
sleep('TP10','y')
plt.show()

