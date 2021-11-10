import numpy as np 
import matplotlib.pyplot as plt
import scipy
from scipy.signal import filtfilt
from scipy import stats
import pandas as pd

df = pd.read_csv (r'C:/Users/UseXtreme/Desktop/ti_green.csv')
print (df)

# Goals:
# 1 - Compute FFT using Numpy "fft" function
# 2 - Plot the frequency spectrum using matplotlib

# Construct a time signal
#Fs = 2000 # sampling frequency
def sleep(haha,col):
    Fs=len(df.timestamps)/60 #all bci recorded is of 1 min
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
    print(len(X_mag))
    i=30
    delta=0
    theta=0
    alpha=0
    beta=0
    gamma=0
    while(i!=7063):
        if(i<240):
            delta+=X_mag[i]
            i+=1
        elif(i<480):
            theta+=X_mag[i]
            i+=1
        elif(i<780):
            alpha+=X_mag[i]
            i+=1
        elif(i<1800):
            beta+=X_mag[i]
            i+=1
        else:
            gamma+=X_mag[i]
            i+=1
    print("delta:",delta," ","theta:",theta," ","alpha:",alpha," ","beta:",beta," ","gamme:",gamma)

    

    f_plot = np.fft.rfftfreq(N,1/Fs)

    plt.plot(f_plot, X_mag,col)

sleep('AF7','r')
sleep('AF8','g')
sleep('TP9','b')
sleep('TP10','y')
plt.show()

