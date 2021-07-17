import pandas as pd

#컬럼명을 미리 잡아둠(추후 컬럼명 에러 방지를 위해)
column = ['순위', '영화명', '개봉일', '매출액', '매출액', '매출액증감', '매출액증감율', '누적매출액', '관객수',
       '관객수증감', '관객수증감율', '누적관객수', '스크린수', '상영횟수', '대표국적', '국적', '배급사']

#df들을 적재할 초기화 해둔 데이터프레임을 생성
df_res = pd.DataFrame([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
], columns = column)

#두번의 반복문을 통해 연도와 주를 받아 해당하는 csv파일을 읽여 들이고 데이터프레임에 적재해 나가는 코드
for year in range(2019, 2022):
    if year == 2019:
        for week in range(1,50,4):
            week_str = str(week)

            df = pd.read_csv('C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/weekly/'+str(year)+'_'+week_str+'.csv')
            df1 = df.rename(columns=df.iloc[0])
            df_res = pd.concat([df_res, df1])
            
    elif year == 2020:
        for week in range(1,54,4):
            week_str = str(week)
            
            df = pd.read_csv('C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/weekly/'+str(year)+'_'+week_str+'.csv')
            df1 = df.rename(columns=df.iloc[0])
            df_res = pd.concat([df_res, df1])
            
    else:        
        for week in range(3,24,4):
            week_str = str(week)
            
            df = pd.read_csv('C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/weekly/'+str(year)+'_'+week_str+'.csv')
            df1 = df.rename(columns=df.iloc[0])
            df_res = pd.concat([df_res, df1])

#적재된 df_res 데이터 프레임에서 필요 없는 정보(열)들을 제거
df_res.drop([df_res.columns[1],df_res.columns[2],
             df_res.columns[6], df_res.columns[7], df_res.columns[10],
            df_res.columns[11], df_res.columns[12], df_res.columns[13],
            df_res.columns[14], df_res.columns[15], df_res.columns[16]], axis=1, inplace = True)

#df_res에서 합계액만 있는 행들을 제외한 행들을 삭제
df_tot = df_res[df_res['순위'] == '합계']

#df_tot의 열이름들을 새롭게 변경
df_tot.columns = ['순위', '매출액', '매출점유율', '매출액증감', '관객수', '관객수증감']
df_tot.drop(['순위', '매출점유율'], axis=1, inplace=True)

#매출액과 관객수의 데이터들에서 특수문자 제거 및 실수형으로 변환
df_tot["매출액"] = df_tot["매출액"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
df_tot["관객수"] = df_tot["관객수"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
df_tot = df_tot.astype({'매출액': 'float'})
df_tot = df_tot.astype({'관객수': 'float'})

df_tot.reset_index(inplace=True)
df_tot.drop([df_tot.columns[0]], axis=1, inplace= True)

#매출액과 관객수를 백만단위로 변환
df_tot['매출액'] = df_tot['매출액'] / 1000000
df_tot['관객수'] = df_tot['관객수'] / 1000000


#매출액에 넣어줄 시리즈 생성
ser1 = pd.Series(df_tot['매출액'])

#매출액 차이를 통해 매출액 변동사항 계산 및 새로운 시리즈에 저장
lst = [0]
for idx in range(1, len(ser1)):
    lst.append((ser1[idx] - ser1[idx-1])/df_tot['매출액'][idx])
    ser2 = pd.Series(lst)

#매출액 증감 열에 위에서 만든 시리즈 대입
df_tot['매출액증감'] = ser2

#매출액과 유사하게 관객수 계산
ser3 = pd.Series(df_tot['관객수'])
lst = [0]
for idx in range(1, len(ser3)):
    lst.append((ser3[idx] - ser3[idx-1])/df_tot['관객수'][idx])
    ser4 = pd.Series(lst)
    
df_tot['관객수증감'] = ser4


#연도와 주차를 넣어줄 리스트 값을 생성 후 변환하여 df-tot의 연도주차 열에 대입하는 과정
lst = []
for year in range(2019, 2022):
    if year == 2019:
        for week in range(1,53):
            yt_week = str(year)+'_'+str(week)
            lst.append(yt_week)
    elif year == 2020:
        for week in range(1,54):
            yt_week = str(year)+'_'+str(week)    
            lst.append(yt_week)
    else:
        for week in range(1,27):
            yt_week = str(year)+'_'+str(week)
            lst.append(yt_week)
ser_yr_wekk = pd.Series(lst)

df_tot['연도주차'] = ser_yr_wekk


#정제한 데이터프레임을 weekly_total.csv로 저장
df_tot.to_csv("./Movie_CSV/weekly_total.csv", index=False)