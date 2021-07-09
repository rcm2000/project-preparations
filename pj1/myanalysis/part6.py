import json

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium as fol
from config.settings import DATA_DIRS, TEMPLATES


df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',
                   header=0)
df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl')
df = df.fillna(method='ffill')
df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=None)
df3.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','modelyear','origin','carname']
tt = sns.load_dataset('titanic');
df4 =  pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl')
df5 =  pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl')

class Part5:
    def p172(self):
        return None



if __name__ == '__main__':
    Part5().p172()