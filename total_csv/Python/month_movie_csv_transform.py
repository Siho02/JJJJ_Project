import numpy as np
import pandas as pd

#1. 2019년 1월~12월 사이의 데이터들을 하나의 통합 csv파일로 변환 하는 과정

#1-1. 통합 csv파일을 위한 새로운 컬럼명을 설정하고 데이터프레임(df_res)를 만듦
column = ['매출액', '관객수', '신작수', '연월']
df_res = pd.DataFrame([
    [0,0,0,'2019']
    ], columns = column)

#1-2. 1월 ~ 12월의 과정 반복합니다.
for month in range(1,13):
    if month < 10 :
        #파일명을('2019_01.csv') 제대로 읽어오기 위해 0을 추가해서 str으로 저장
        month_str = '0'+str(month)
    else :
        month_str = str(month)

    #csv 파일 2019_01 ~ 2019_12를 읽어 데이터 프레임 생성
    df= pd.read_csv('C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/month/2019'+month_str+'.csv')

    #추후에 저장할 날짜와 상세 날짜 변수를 잡아둠
    date = '2019-'+month_str
    detail_date = '2019'+month_str+'01'

    #df로 만들어낸 데이터프레임의 0번째 컬럼을 삭제 (0번째 컬럼 : '0 NaN NaN NaN NaN 점유율'인 불필요한 데이터)
    df1 = df.drop(df.index[0])

    #필요하지 않은 데이터열 삭제(순위, 영화명, 매출액점유율 등..)
    df1.drop([df1.columns[0], df1.columns[1], df1.columns[4], df1.columns[5], df1.columns[7]], axis=1, inplace=True)
    df1.drop([df1.columns[3], df1.columns[4], df1.columns[5], df1.columns[6], df1.columns[7]], axis=1, inplace=True)

    #그 달의 개봉작 숫자를 세기 위한 열 추가 및 0으로 초기화
    df1['신작수'] = 0
    #개봉일이 null값인 경우 그달의 개봉작이 아니므로 none이라는 값으로 대체
    df1['개봉일'].fillna('none', inplace=True)
    
    
    #df_len : 데이터 프레임의 열 개수
    df_len = len(df1['개봉일'])
    for idx in range(1,df_len):
        #개봉일의 데이터 0~6번째 값이 date(예를 들어 2019-01)와 같은 경우 신작수 열에 1을 추가
        if df1['개봉일'][idx][0:7] == date:
            df1['신작수'][idx] = 1

    #신작의 개수를 세기 위해 tot값을 잡아둔 후 반복문을 통해 모든 신작수를 받아옴
    tot = 0
    for idx in range(1,df_len):
        tot += df1['신작수'][idx]

    #총합을 저장하는 열에 tot값을 대입
    df1['신작수'][df_len] = tot

    #영화 하나하나의 정보를 저장한 행들을 모두 제거
    df1.drop(df1.index[0:df_len-1], inplace=True)

    #데이터 프레임에 새로운 열을 추가한 후 detail_date(20190101, 20190201 등을 추가
    df1['연월'] = detail_date

    #인덱스를 초기화
    df1.reset_index(inplace=True)
    df1.drop([df1.columns[0], df1.columns[1]], axis=1, inplace=True)

    #       매출액        관객수   신작수  연월
    #0  30,158,665,300  3,256,510  205   20210301

    # df_res에 반복해 나오는 df1을 적재해나감
    df_res = pd.concat([df_res, df1])


df_res.drop([df_res.columns[0], df_res.columns[1]], axis=1, inplace=True)
df_res.reset_index(inplace=True)
df_res.drop([df_res.index[0]], inplace = True)

#나온 df_res 1~4 열을 df_res19에 저장
df_res19 = df_res[df_res.columns[1:5]]




#2. 2020년 1월~12월 사이의 데이터들을 하나의 통합 csv파일로 변환 하는 과정
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


#3. 2020년 1월~12월 사이의 데이터들을 하나의 통합 csv파일로 변환 하는 과정
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


#1 ~ 3과정에서 만들어낸 19,20,21년 데이터 프렝미을 합쳐서 최종 df_total을 생성
df_total = pd.concat([df_res19, df_res20, df_res21])

#df_total의 관객수 및 매출액 열을 백만단위로 변경
df_total[df_total.columns[2]] = df_total[df_total.columns[2]].str.replace(pat=r'[^\w]', repl=r'', regex=True)
df_total[df_total.columns[3]] = df_total[df_total.columns[3]].str.replace(pat=r'[^\w]', repl=r'', regex=True)
df_total = df_total.astype({df_total.columns[2]: 'float'})
df_total = df_total.astype({df_total.columns[3]: 'float'})

df_total[df_total.columns[2]] = df_total[df_total.columns[2]] / 1000000
df_total[df_total.columns[3]] = df_total[df_total.columns[3]] / 1000000

#df_total을 csv로 저장
df_total.to_csv("C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/monthly_total.csv", index=False)
