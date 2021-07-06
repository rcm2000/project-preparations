import pandas as pd
import matplotlib.pyplot as plt

from config.settings import DATA_DIRS
ddf = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl')
df = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv')
ddf = ddf.fillna(method='ffill')
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','modelyear','origin','carname']
class P084:
    def df01(self):
        print(df.head())
        print(df.shape,df.info())
        print(df.describe(include='all'))
    def df02(self):
        uv = df['origin'].value_counts()
        print(uv)
        df2 = df[['mpg','weight']].mean();
        print(df2)
        df3 = df[df['mpg']>df['mpg'].mean()]
        print(df3)
    def df03(self):
        print(ddf)
        ddf2 = ddf.iloc[[0,5],3:]
        ddf2.index = ['south','north']
        print(ddf2)
        ddf2.columns = ddf2.columns.map(int)
        plt.plot(ddf2)
        plt.show()
        ddf2t = ddf2.T
        print(ddf2t)





if __name__  == '__main__':
    P084().df03()