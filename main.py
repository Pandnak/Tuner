import importlib
moduleName = 'FFT.py'
importlib.import_module(moduleName)

from IPython.display import Audio
import matplotlib.pyplot as plt # импорт модуля matplotlib.pyplot
import scipy.io.wavfile
Audio('tuning-fork.wav')
fs, x = scipy.io.wavfile.read('tuning-fork.wav')

x1=x[8000:10000]                     # выбор наблюдаемого диапазона
k=np.arange(x1.size)               # отсчеты по времени
# Построение графиков 
plt.figure(figsize=[16, 4])         # создание полотна размером шириной 8 X 4 дюйма
plt.plot(k/fs, x1, 'b.')           # построение графика цифрового сигнала точками точками
plt.grid()                             
plt.xlabel("$t$, c")                      
plt.ylabel("$x[k]$") 