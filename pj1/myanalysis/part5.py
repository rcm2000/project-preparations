import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium as fol
from config.settings import DATA_DIRS, TEMPLATES
from sklearn import preprocessing


df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',
                   header=0)
df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl')
df = df.fillna(method='ffill')
df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=None)
df3.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','modelyear','origin','carname']
tt = sns.load_dataset('titanic');
df4 =  pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl')
df5 =  pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl')
st = pd.read_csv(DATA_DIRS[0]+'//stock-data.csv')
class Part5:
    def p172(self):
        print(tt.info())
        print(tt['deck'].value_counts(dropna=False))
        print(tt.isnull().sum())
        #thresh로 결측치가 n개 이상인 열을 삭제
        ttage = tt.dropna(subset=['age'],how='any',axis=0)
        tt1 = tt.dropna(axis=1,thresh=500)
        # print(tt1)
        # print(tt1.shape)
        # print(tt1.isnull().sum())
        print(ttage)
    def p178(self):
        mage = tt['age'].mean();
        print(mage)
        tt['age'].fillna(mage,inplace=True)
        print(tt['age'])

    def p180(self):
        et = tt['embark_town'].value_counts().idxmax()
        print(et)
        tt['embark_town'].fillna(et,inplace=True)
    def p181(self):
        tt['embark_town'].fillna(method='ffill', inplace=True)
    def p186(self):
        print(df3)
        mpg_to_kpl = 1.60934/3.78541
        df3['kpl'] = (df3['mpg'] * mpg_to_kpl).round(2)
        print(df3)
    def p188(self):
        print(df3.info())
        df3['horsepower'].replace('?',np.NaN,inplace=True)
        print(df3['horsepower'].unique())
        df3.dropna(subset=['horsepower'],axis=0,inplace=True)
        df3['horsepower'] = df3['horsepower'].astype('float')
        print(df3['horsepower'])
    def p190(self):
        print(df3.info())
        print(df3['origin'].unique())
        df3['origin'].replace({1:'USA',2:'EU',3:'JPN'},inplace=True)
        df3['origin'] = df3['origin'].astype('category')
        print(df3['origin'].dtypes)
    def p192(self):
        df3['horsepower'].replace('?', np.NaN, inplace=True)
        print(df3['horsepower'].unique())
        df3.dropna(subset=['horsepower'], axis=0, inplace=True)
        df3['horsepower'] = df3['horsepower'].astype('float')
        cnt, bin_dividers = np.histogram(df3['horsepower'],bins = 3)
        print(cnt,bin_dividers)
        bin_names = ['고','중','저']
        df3['hp_bin'] = pd.cut(
            x=df3['horsepower'],
            bins = bin_dividers,
            labels=bin_names,
            include_lowest=True

        )
        hp_dum = pd.get_dummies(df3['hp_bin'])
        print(hp_dum)
        lable_encoder = preprocessing.LabelEncoder()
        onehot_encoder = preprocessing.OneHotEncoder()
        onehot_labled = lable_encoder.fit_transform(df3['hp_bin'].head(15))
        print(onehot_labled)
    def p198(self):
        df3['horsepower'].replace('?', np.NaN, inplace=True)
        df3.dropna(subset=['horsepower'], axis=0, inplace=True)
        df3['horsepower'] = df3['horsepower'].astype('float')

        df3['horsepower'] = df3['horsepower']/abs(df3['horsepower'].max())
        print(df3['horsepower'])
    def p201(self):
        print(st)
        print(st.info())
        st['new_Date'] = pd.to_datetime(st['Date'])
        print(st)
        print(st.info())
        print(st['new_Date'][0])
        st.set_index(st['new_Date'],inplace=True)
        print(st)
    def p205(self):
        dates = ['2019-01-01','2020-03-01','2021-06-01']

        ts_dates = pd.to_datetime(dates)
        print(ts_dates)

        pr_day = ts_dates.to_period(freq='D')
        pr_month = ts_dates.to_period(freq='M')
        pr_year = ts_dates.to_period(freq='A')
        print(pr_day)
        print(pr_month)
        print(pr_year)
    def p206(self):
        ts_ms = pd.date_range(
            start = '2020-01-01',
            end=None,
            periods=6,
            freq='MS',
            tz='Asia/seoul')
        print(ts_ms)

        pr_ms = pd.period_range(
            start='2020-01-01',
            end=None,
            periods=6,
            freq='M')
        print(pr_ms)
    def p209(self):
        st['new_Date'] = pd.to_datetime(st['Date'])
        st.set_index(st['new_Date'],inplace=True)
        print(st)
        st['Year'] = st.index.dt
    def p212(self):
        st['new_Date'] = pd.to_datetime(st['Date'])
        st.set_index(st['new_Date'], inplace=True)
        print(st)

        st_y = st.loc['2018-06-05':'2018-06-01','High':'Low']
        print(st_y)




if __name__ == '__main__':
    Part5().p212()