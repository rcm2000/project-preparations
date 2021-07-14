import json

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium as fol
from config.settings import DATA_DIRS, TEMPLATES, STATICFILES_DIRS

df = pd.read_excel(DATA_DIRS[0]+'//data1.xlsx',engine='openpyxl',
                   header=0)
df2 = pd.read_excel(DATA_DIRS[0]+'//data2.xlsx',engine='openpyxl')
df = df.fillna(method='ffill')
df3 = pd.read_csv(DATA_DIRS[0]+'//auto-mpg.csv',header=None)
df3.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','modelyear','origin','carname']
tt = sns.load_dataset('titanic');
df4 =  pd.read_excel(DATA_DIRS[0]+'//data3.xlsx',engine='openpyxl')
df5 =  pd.read_excel(DATA_DIRS[0]+'//data4.xlsx',engine='openpyxl')

class WS01:
    def chart01(self,tran_place):
        mask = (df['전출지별'] == tran_place) & (df['전입지별'] != '서울특별시')
        df_seoul = df[mask]
        df_seoul = df_seoul.drop(['전출지별'], axis=1)
        df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
        df_seoul.set_index('전입지', inplace=True)
        # print(df_seoul)
        df3 = df_seoul.loc[['강원도', '충청북도', '경상북도', '전라남도']]
        # print(df3.sum(axis=1))
        # df3.loc['년도계'] = df3.sum()
        # df3['합계'] = df3.sum(axis=1)
        print(df3)
        print(df3.index.tolist())
        print(df3.iloc[0].tolist())
        result = []
        for i in range(0,4):
            print(df3.index[i])
            print(df3.iloc[i].tolist())
            result.append({
            'name': df3.index[i],
            'data': df3.iloc[i].tolist()
            })
        print(result)
        return result
    def chart02(self,first,end):
        # print(df2)
        df3 = df2.loc[5:9]
        df3.drop('전력량 (억㎾h)', axis=1, inplace=True)
        df3.set_index('발전 전력별', inplace=True)
        # print(df3)
        df3t = df3.T
        df3t.drop('원자력', axis=1, inplace=True)
        # print(df3t)
        df3t = df3t.rename(columns={'합계': '총발전량'});
        df3t['1년전'] = df3t['총발전량'].shift(1)
        df3t['증감률'] = ((df3t['총발전량'] / df3t['1년전']) - 1) * 100;
        df3t.fillna(0,inplace = True)
        # print(df3t)
        df4 = df3t.loc[first:end,:]
        # print(df4)
        # print(df4['수력'].tolist())
        # print(df4['화력'].tolist())
        # print(df4['증감률'].tolist())
        # print(df4.index.tolist())
        result1 = [{
        'type': 'column',
        'name': '수력',
        'data': df4['수력'].tolist()
    }, {
        'type': 'column',
        'name': '화력',
        'data': df4['화력'].tolist()
    }, {
        'type': 'spline',
        'name': '증감률',
        'data': df4['증감률'].tolist(),
    }]
        result2 = df4.index.tolist()

        result = result1,result2
        return result
    def chart03(self):
        sns.set_style('whitegrid')

        fig = plt.figure(figsize=(15,5))
        ax1 = fig.add_subplot(1,3,1)
        ax2 = fig.add_subplot(1, 3, 2)
        ax3 = fig.add_subplot(1, 3, 3)

        sns.barplot(x='sex',y = 'survived',data = tt,ax = ax1)
        sns.barplot(x='sex', y='survived',hue = 'class', data=tt, ax=ax2)
        sns.barplot(x='sex', y='survived', hue='class',dodge = False, data=tt, ax=ax3)

        ax1.set_title('titanic survived = sex')
        ax2.set_title('titanic survived = sex/class')
        ax3.set_title('titanic survived = sex/class(stacked)')

        # plt.show()
        plt.savefig(STATICFILES_DIRS[0]+'\\tt_fig1.png', dpi=300,facecolor='#eeeeee')

    def chart04(self,year):
        year = int(year)
        df5.set_index('구분', inplace=True)
        print(df5)
        geo_path = DATA_DIRS[0] + '/data4.json'
        geo_data = json.load(open(geo_path), encoding='utf-8')
        map = fol.Map(location=[37.55, 126.98], zoom_start=9);
        fol.Choropleth(
            geo_data=geo_data,
            data=df5[year],
            columns=[df5.index, df5[year]],
            fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
            threshold_scale=[10000, 100000, 300000, 500000, 700000],
            key_on='feature.properties.name'
        ).add_to(map)
        print(geo_data)
        map.save(TEMPLATES[0]['DIRS'][0] + '\\gyonggi.html')

        return year



if __name__  == '__main__':
    WS01().chart04('2007')


