import numpy as np 

def dtft(x, M=2048):
    return  np.arange(M)/M - 1/2, np.fft.fftshift(np.fft.fft(x, M))

def DFT(x):
    N = len(x)
    X = np.array(N)
    for k in range(0, N-1):
        X[k] = sum(x[n]*np.exp(-2*np.pi*k*n/N))
    return X

def inverseDFT(X):
    N = len(X)
    x = np.array(N)
    for n in range(0, N-1): 
            x[n] = (1/N)*sum(X[k]*np.exp(2*np.pi*k*n/N))
    return x