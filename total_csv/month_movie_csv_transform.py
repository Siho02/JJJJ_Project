import numpy as np
import pandas as pd

column = ['매출액', '관객수', '신작수', '연월']
df_res = pd.DataFrame([
    [0,0,0,'2019']
    ], columns = column)

for month in range(1,13):
    if month < 10 :
        month_str = '0'+str(month)
    else :
        month_str = str(month)

    df= pd.read_csv('C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/month/2019'+month_str+'.csv')

    date = '2019-'+month_str
    detail_date = '2019'+month_str+'01'
    df1 = df.drop(df.index[0])
    df1.drop([df1.columns[0], df1.columns[1], df1.columns[4], df1.columns[5], df1.columns[7]], axis=1, inplace=True)
    df1.drop([df1.columns[3], df1.columns[4], df1.columns[5], df1.columns[6], df1.columns[7]], axis=1, inplace=True)
    df1['신작수'] = 0
    df1['개봉일'].fillna('none', inplace=True)

    df_len = len(df1['개봉일'])

    for idx in range(1,df_len):
        if df1['개봉일'][idx][0:7] == date:
            df1['신작수'][idx] = 1

    tot = 0
    for idx in range(1,df_len):
        tot += df1['신작수'][idx]

    df1['신작수'][df_len] = tot

    df1.drop(df1.index[0:df_len-1], inplace=True)
    df1['연월'] = detail_date
    df1.reset_index(inplace=True)

    df1.drop([df1.columns[0], df1.columns[1]], axis=1, inplace=True)
    
    df_res = pd.concat([df_res, df1])

df_res.drop([df_res.columns[0], df_res.columns[1]], axis=1, inplace=True)
df_res.reset_index(inplace=True)
df_res.drop([df_res.index[0]], inplace = True)
df_res19 = df_res[df_res.columns[1:5]]



column = ['매출액', '관객수', '신작수', '연월']
df_res = pd.DataFrame([
    [0,0,0,'2020']
    ], columns = column)

for month in range(1,13):
    if month < 10 :
        month_str = '0'+str(month)
    else :
        month_str = str(month)

    df= pd.read_csv('C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/month/2020'+month_str+'.csv')

    date = '2020-'+month_str
    detail_date = '2020'+month_str+'01'
    df1 = df.drop(df.index[0])
    df1.drop([df1.columns[0], df1.columns[1], df1.columns[4], df1.columns[5], df1.columns[7]], axis=1, inplace=True)
    df1.drop([df1.columns[3], df1.columns[4], df1.columns[5], df1.columns[6], df1.columns[7]], axis=1, inplace=True)
    df1['신작수'] = 0
    df1['개봉일'].fillna('none', inplace=True)

    df_len = len(df1['개봉일'])

    for idx in range(1,df_len):
        if df1['개봉일'][idx][0:7] == date:
            df1['신작수'][idx] = 1

    tot = 0
    for idx in range(1,df_len):
        tot += df1['신작수'][idx]

    df1['신작수'][df_len] = tot

    df1.drop(df1.index[0:df_len-1], inplace=True)
    df1['연월'] = detail_date
    df1.reset_index(inplace=True)

    df1.drop([df1.columns[0], df1.columns[1]], axis=1, inplace=True)
    
    df_res = pd.concat([df_res, df1])

df_res.drop([df_res.columns[0], df_res.columns[1]], axis=1, inplace=True)
df_res.reset_index(inplace=True)
df_res.drop([df_res.index[0]], inplace = True)
df_res20 = df_res[df_res.columns[1:5]]


column = ['매출액', '관객수', '신작수', '연월']
df_res = pd.DataFrame([
    [0,0,0,'2021']
    ], columns = column)

for month in range(1,7):
    if month < 10 :
        month_str = '0'+str(month)
    else :
        month_str = str(month)
    df= pd.read_csv('C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/month/2021'+month_str+'.csv')

    date = '2021-'+month_str
    detail_date = '2021'+month_str+'01'
    df1 = df.drop(df.index[0])
    df1.drop([df1.columns[0], df1.columns[1], df1.columns[4], df1.columns[5], df1.columns[7]], axis=1, inplace=True)
    df1.drop([df1.columns[3], df1.columns[4], df1.columns[5], df1.columns[6], df1.columns[7]], axis=1, inplace=True)
    df1['신작수'] = 0
    df1['개봉일'].fillna('none', inplace=True)

    df_len = len(df1['개봉일'])

    for idx in range(1,df_len):
        if df1['개봉일'][idx][0:7] == date:
            df1['신작수'][idx] = 1

    tot = 0
    for idx in range(1,df_len):
        tot += df1['신작수'][idx]

    df1['신작수'][df_len] = tot

    df1.drop(df1.index[0:df_len-1], inplace=True)
    df1['연월'] = detail_date
    df1.reset_index(inplace=True)

    df1.drop([df1.columns[0], df1.columns[1]], axis=1, inplace=True)
    
    df_res = pd.concat([df_res, df1])

df_res.drop([df_res.columns[0], df_res.columns[1]], axis=1, inplace=True)
df_res.reset_index(inplace=True)
df_res.drop([df_res.index[0]], inplace = True)
df_res21 = df_res[df_res.columns[1:5]]

df_total = pd.concat([df_res19, df_res20, df_res21])
df_total.to_csv("C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/monthly_total.csv", index=False)
