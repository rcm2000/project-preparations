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
stock = pd.read_excel(DATA_DIRS[0]+'//stock.xlsx',engine='openpyxl')
stock_price = pd.read_excel(DATA_DIRS[0]+'//stock price.xlsx',engine='openpyxl')
stock_val = pd.read_excel(DATA_DIRS[0]+'//stock valuation.xlsx',engine='openpyxl')
class Util:
    def add10(self,n):
        return n + 10
    def add_two_obj(self,a,b):
        return a+b
    def min_max(self,x):
        return x.max() - x.min()
    def kpl(self,mpg,cyl):
        return mpg * (1.6/3.7) +cyl
    def total(self,df):
        return df.isnull()
    def m_value(self,x):
        return x.isnull()
    def m_count(self,x):
        return self.m_value(x).sum()
    def display(self,df):
        return df.info()

class Part6:
    def p218(self):
        df = tt.loc[:,['age','fare']]
        df['ten'] = 10
        print(df)
        df2 = df['age'].apply(Util().add10)
        print(df2)
        df3 = df['age'].apply(Util().add_two_obj,b=20)
        print(df3)
        df4 = df['age'].apply(lambda x:x+10)
        print(df4)
        return None
    def p221(self):
        # tt.apply(Util().add10)
        df = tt.loc[:,['age','fare']]
        df2 = df.apply(Util().add10)
        print(df2)

    def p221test(self):
        print(df3)
        df3['kpl'] = df3.apply(lambda x:Util().kpl(x['mpg'],x['cylinders']),axis = 1)
        print(df3)
    def p226(self):
        result = tt.pipe(Util().display)
        print(result)
        result2 = tt.pipe(Util().total)
        print(result2)
    def p229(self):
        df = tt.loc[0:4,'survived':'age']
        print(df)
    def p234(self):
        mask = (tt['age'] >= 10) & (tt['age'] <20)
        mask2 = (tt['age'] >= 10) & (tt['sex'] == 'female')
        mask3 = (tt['age'] < 10) & (tt['age'] >= 60)
        tt2 = tt.loc[mask2,['age','sex','pclass']]
        print(tt2)
        pd.set_option('display.max_columns',10)
        mask10 = tt['sibsp'] == 3
        mask20 = tt['sibsp'] == 4
        mask30 = tt['sibsp'] == 5
        tt3 = tt[mask10|mask20]
        print(tt3)
    def p240(self):
        df1 = pd.DataFrame({
            'a': ['a0','a1','a2','a3'],
            'b': ['b0', 'b1', 'b2', 'b3'],
            'c': ['c0', 'c1', 'c2', 'c3'],
            'd': ['d0', 'd1', 'd2', 'd3'],
        },index=[0,1,2,3])
        df2 = pd.DataFrame({
            'a': ['a2', 'a3', 'a4', 'a5'],
            'b': ['b2', 'b3', 'b4', 'b5'],
            'c': ['c2', 'c3', 'c4', 'c5'],
            'd': ['d2', 'd3', 'd4', 'd5'],
        }, index=[2, 3, 4, 5])
        result1 = pd.concat([df1,df2])
        print(result1)
        result2 = pd.concat([df1, df2],axis=1)
        print(result2)

        sr1 = pd.Series(['e0','e1','e2','e3'],name='e')
        sr2 = pd.Series(['f0', 'f1', 'f2'], name='f')
        sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')
        print(sr2)
        result3 = pd.concat([df1,sr1],axis =1)
        print(result3)
        result4 = pd.concat([df2,sr2],axis=1)
        print(result4)
    def p245(self):
        print(stock_val)
        df1 = pd.merge(stock_price,stock_val, on = None,how='inner')
        df2 = pd.merge(stock_price, stock_val, how='left',
                       left_on='stock_name',right_on='name')
        print(df2)
        price = stock_price[stock_price['price']<50000]
        print(price)
        value = pd.merge(price,df2)
        print(value)
    def p252(self):
        stock_price.set_index(stock_price['id'],inplace=True)
        stock_val.set_index(stock_val['id'], inplace=True)
        df3 = stock_price.join(stock_val)
        print(df3)
    def p254(self):
        df = tt.loc[:,['age','sex','class','fare','survived']]
        print(df)
        gdf = df.groupby(['class'])
        print(gdf)
        print(gdf.mean())

        gdf2 = df.groupby(['class','sex'])
        gdf2_mean = gdf2.mean()
        print(gdf2_mean)
        g1 = gdf2.get_group(('First','female'))
        print(g1)

    def p261(self):
        df = tt.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        print(df)
        gdf = df.groupby(['class'])
        print(gdf)
        print(gdf.mean())
        print(gdf['fare'].mean())
    def p271(self):
        df = tt.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        print(df)
        grouped= df.groupby(['class','sex'])

        gdf = grouped.mean()
        print(gdf)
        print(gdf.loc['First'])
        print(gdf.xs('male',level='sex'))

    def p273(self):
        pd.set_option('display.max_columns',10)
        pd.set_option('display.max_colwidth', 20)
        df = tt.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        print(df.head())
        pdf = pd.pivot_table(df,
                             index='class',
                             columns='sex',
                             values='survived',
                             aggfunc=['mean','sum'])
        print(pdf)

        print(df.rename({'sex':'sex1'}, axis=1))


if __name__ == '__main__':
    Part6().p273()