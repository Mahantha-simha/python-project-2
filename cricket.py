import pandas as pd
import re
import numpy as np

data=pd.read_csv('cricket.csv')
data.drop(data.columns[0], axis=1, inplace=True)
# print(data.columns)

df=data.copy()

# print(df.head())

df['Country'] = df['Player'].str.extract(r'\((\w+)\)')
df['Player'] = df['Player'].str.replace(r'\((\w+)\)'," ", regex=True)
df['Player']=df['Player'].str.strip()

loc=df.columns.get_loc('Player') + 1
colos=list(df.columns)
colos.insert(loc, colos.pop(colos.index('Country')))
df=df[colos]

# print(df['Country'].unique())

# x= df[df['Player']== "AB de Villiers"]
# print(x)   

df=df.rename(columns={'NO':'Not_Out', 'HS':'Higest_Score','BF':'Balls','SR':'Strike_rate','Mat':'Matches'})
# print(df.columns)

df = df.applymap(lambda x: np.nan if x == '-'  else x )
df['Strike_rate']=df['Strike_rate'].fillna(0)
df['Balls']=df['Balls'].fillna(0)


x=data.drop_duplicates(inplace=True)
print(data[data['Player']=='KF Barrington (ENG)'])
df['First_year']=df['Span'].str.split(pat ='-').str[0]
df['Final_year']=df['Span'].str.split(pat ='-').str[1]
df.drop(['Span'], axis=1, inplace=True)  # Modify in place



print(df)
# print(x)
# print(df[df['Strike_rate']==0])



# df.to_csv('modefied.csv',index=0) 