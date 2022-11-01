import pandas as pd
data = pd.read_csv('subset-covid-data.csv',encoding='UTF-8')
print(data.head)
data.info()