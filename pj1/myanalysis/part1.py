import pandas as pd
data = {
            '수학': [90, 80, 70],
            '영어': [91, 81, 71],
            '과학': [92, 82, 72],
            '국어': [93, 83, 73],

        }
df = pd.DataFrame(data, index=['A', 'B', 'C'])


class P001:
    def series01(self):
        list_data = ['202007',3.14,'ABC',100,True]
        sr = pd.Series(list_data)
        sr2 = sr.tolist()
        print(sr);
        print(sr2);
        print(sr.values);
        print(sr.index);
        print(sr[[1,4]]);
    def df01(self):

        print(df)
        df2 = df.copy();
        df2.drop(['수학','국어'],axis=1,inplace=True)
        print(df2)
    def df02(self):

        print(df)
        df2 = df.copy();
        df2.drop(['A','B'],inplace=True)
        print(df2)
    def df03(self):

        print(df)
        data1 = df.loc['B'];
        print(data1)
        data2 = df.iloc[[1,2]]
        print(data2)
    def df04(self):
        print(df)
        df['이름'] = ['영희','철수','민철']
        # s1 = df[['영어','국어']]
        # print(s1)
        # s2 = df.iloc[:,1:]
        # print(s2)

        df.set_index('이름',inplace=True)
        print(df)
        d1 = df.loc['영희','수학':'과학']
        d2 = df.iloc[0,0:3]
        print(d2)
    def df05(self):
        print(df)
        df.loc['D'] = [99,88,77,66]
        df2 = df.reset_index()
        df3 = df2.sort_index(ascending=False)
        print(df)

        df4 = df2.sort_values(by='수학')
        print(df4)
        # df2 = df.transpose()
        # print(df2)
        
if __name__ == '__main__':
    P001().df05();
