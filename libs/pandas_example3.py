import pandas as pd
import os

cwd=os.getcwd()
'''
archivo=cwd + "/libs/vital_signs.csv"

vital_signs=pd.read_csv(archivo,index_col='timestamp',parse_dates=True )

#calculasla frecuencia promedio por hora 
heart_rate=vital_signs['heart_rate'].resample('1H').mean()
print(heart_rate)
'''
archivo = cwd + "/libs/patient_data.csv"
patient_data=pd.read_csv(archivo)
archivo2= cwd + "/libs/population_data.csv"
population_data=pd.read_csv(archivo2)

merge_data=pd.merge(patient_data,population_data,on="Zip Code")
print(merge_data)

merge_data['Chronic Condition %'] = merge_data['Chronic Condition Count']/merge_data['Population']*100 
print(merge_data)
