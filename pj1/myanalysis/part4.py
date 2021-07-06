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

class P109:
    def mat01(self):
        print(df)
        mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
        df_seoul = df[mask]
        df_seoul = df_seoul.drop(['전출지별'], axis=1)
        df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
        df_seoul.set_index('전입지', inplace=True)
        sr_one = df_seoul.loc['경기도']
        shead = sr_one.head()
        # print(shead)
        # plt.plot(sr_one.index,sr_one.values);
        # plt.show()
        # print(sr_one)
        result = [];
        d = {}
        d['name'] = '경기도'
        d['data'] = sr_one.values.tolist()
        result.append(d)
        print(result)
    def mat02(self):

        mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
        df_seoul = df[mask]
        df_seoul = df_seoul.drop(['전출지별'], axis=1)
        df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
        df_seoul.set_index('전입지', inplace=True)
        print(df_seoul)
        df3 = df_seoul.loc[['경기도','강원도','충청북도','전라남도']]
        df3t = df3.T
        print(df3t)
        plt.style.use('ggplot');
        df3t.index = df3t.index.map(int)


    def mat03(self):
        mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
        df_seoul = df[mask]
        df_seoul = df_seoul.drop(['전출지별'], axis=1)
        df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
        df_seoul.set_index('전입지', inplace=True)
        print(df_seoul)
        df3 = df_seoul.loc[['충청남도', '강원도', '충청북도', '전라남도']]
        print(df3.sum(axis=1))
        df3.loc['년도계'] = df3.sum()
        df3['합계'] = df3.sum(axis=1)
        print(df3)
    def mat04(self):
        print(df2)
        df3 = df2.loc[5:9]
        df3.drop('전력량 (억㎾h)', axis = 1,inplace = True)
        df3.set_index('발전 전력별',inplace = True)
        print(df3)
        df3t = df3.T
        df3t.drop('원자력',axis = 1, inplace = True)
        print(df3t)
        df3t = df3t.rename(columns = {'합계':'총발전량'});
        print(df3t)
        df3t['1년전'] = df3t['총발전량'].shift(1)
        df3t['증감률'] = ((df3t['총발전량']/df3t['1년전'])-1)*100;

        print(df3t)
    def mat05(self):
        # 국가별 차량의 개수
        print(df3)
        df3['count'] = 1
        df4 = df3.groupby('origin').sum()
        df4.index = ['USA','EU','JPN']
        print(df4)
    def mat06(self):
        df4 = df3[df3['origin']==1]['mpg']
        print(df4)
    def mat07(self):
        print(tt)
        tt2 = tt.pivot_table(index=['sex'],columns=['class'],aggfunc='size')
        print(tt2)

    def mat08(self):
        seoul_map = fol.Map(location=[37.55,126.98],zoom_start=12);
        seoul_map.save(TEMPLATES[0]['DIRS'][0]+'\\seoul_map.html')

    def mat09(self):
        seoul_map = fol.Map(location=[37.55, 126.98], zoom_start=12);
        print(df4)
        df4.columns = ['name','lat','lng']
        df4.set_index(['name'],inplace=True)
        for name,lat,lng in zip(df4.index,df4['lat'],df4['lng']):
            print(name,lat,lng)
            fol.Marker([lat,lng],popup=name).add_to(seoul_map)
        seoul_map.save(TEMPLATES[0]['DIRS'][0] + '\\seoul_coll.html')
    def mat10(self):
        df5.set_index('구분',inplace=True)
        # print(df5)
        geo_path = DATA_DIRS[0]+'/data4.json'
        geo_data = json.load(open(geo_path),encoding='utf-8')
        map = fol.Map(location=[37.55, 126.98], zoom_start=9);
        fol.Choropleth(
            geo_data=geo_data,
            data=df5[2017],
            columns=[df5.index,df5[2017]],
            fill_color='YlOrRd',fill_opacity=0.7,line_opacity=0.3,
            threshold_scale=[10000,100000,300000,500000,700000],
            key_on='feature.properties.name'
        ).add_to(map)
        print(geo_data)
        map.save(TEMPLATES[0]['DIRS'][0] + '\\gyonggi.html')
if __name__  == '__main__':
    P109().mat10()

