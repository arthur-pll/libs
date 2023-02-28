import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import math

cwd=os.getcwd()
archivo=cwd+ "/libs/ecg_data.csv"
ecg_data=pd.read_csv(archivo)

time=ecg_data['time']
signal=ecg_data['signal']

descripcion = ecg_data['signal'].describe()
#print(descripcion)

#print(ecg_data['signal'].head(50))
#print(ecg_data['signal'].tail(50))

promedio = np.mean(ecg_data.signal)
#print(promedio)

promedio_dinamico=pd.DataFrame.rolling(ecg_data.signal,window=(100)).mean()
#print(promedio_dinamico)
#listas comprensivas
promedio_dinamico=[promedio*1.2 if math.isnan(x*1.2) else (x*1.2) for x in promedio_dinamico]
#print(promedio_dinamico)
ecg_data['promedio_dinamico']=promedio_dinamico

#deteccion de picos
count=0
rango=[]
xmax=[]
ymax=[]
for punto in ecg_data.signal:
    if (punto<=ecg_data.promedio_dinamico[count]) and (len(rango)<1):
        count+=1
    elif punto>ecg_data.promedio_dinamico[count]:
        rango.append(punto)
        count+=1
    else:
        maximo=max(rango)
        ymax.append(maximo)
        maximox=count-len(rango)+rango.index(maximo)
        xmax.append(maximox)

        rango=[]
        count+=1
count=0
dist=[]
while count<len(xmax)-1:
    distancia = xmax[count+1] - xmax[count]
    distancia= distancia/100
    dist.append(distancia)
    count+=1
bpm = 60/np.mean(dist)

print ("BPM:", round(bpm,1))

#'''
plt.plot(time,signal)
plt.plot(ecg_data.promedio_dinamico,color="red")
plt.scatter(xmax,ymax,color="orange",label=bpm)
plt.xlabel('Time (s)')
plt.ylabel("ECG signal (mV)")
plt.title('ECG signal Over Time')
plt.legend(loc=4,framealpha=0.6)
plt.show()
#'''