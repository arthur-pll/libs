import pandas as pd
import os

cwd=os.getcwd()
print(cwd)
archivo=cwd+ "/libs/medical_data.csv"
data=pd.read_csv(archivo)


print(data)
print(data.columns)
print(data['Age'])
print(data.describe())
print(data.head())
print(data.tail())

clean_data=data.dropna()
print(clean_data)
average_age=clean_data['Age'].mean()

print("Edad promedio :", average_age)