import pandas as pd
import numpy as np
# 판다스 : 데이터 분석과 조작을 위한 라이브러리, 데이터를 구조화하고, 저장, 처리, 분석을 수행

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
print(s1.index)
print(s1.values)
print(s1.dtype)

# 판다스는 원소의 데이터 타입이 달라도 가능
s2 = pd.Series(['a', 'b', 'c', 1,2,3])
print(s2)
print(s2.dtype)

# 데이터가 없는 경우 넘파이 np.nan으로 표시 가능
s3 = pd.Series([np.nan, 10, 30])
print(s3)

# Series 데이터 생성 시 인덱스 추가 기능
index_date = ['2023-09-15', '2023-09-16', '2023-09-17', '2023-09-18']
s4 = pd.Series([200, 195, np.nan, 345], index=index_date)
print(s4)

# 파이썬의 딕셔너리 이용
s5 = pd.Series({"국어": 100, "영어": 95, "수학": 90})
print(s5)

# 날짜 자동 생성 : date_range
s6 = pd.date_range(start='2023-09-16', end='2023-10-10')
print(s6)

# 달력을 요일 기준으로 일주일씩 증가
s7 = pd.date_range(start='2023-09-16', periods=4, freq='W')
print(s7)

# 데이터 프레임 : 데이터를 다룰 때 가장 많이 사용하는 데이터 형태, 행과 열로 구성된 사각형 모양의 표
df = pd.DataFrame({'name' : ['james', 'kane', 'justice','cry','samuel'],
                   'kor' : [90, 88, 97, 77, 92],
                   'eng': [80,92,78,95,76]
                   })
print(df)
print(df['kor'])
print(sum(df['kor']/df['kor'].size)) # 평균 구하기

# 실습문제
df_fruit = pd.DataFrame({
    '제품' : ['apple', 'strawberry', 'watermelon'],
    '가격' : [1800, 1500, 3000],
    '판매량' : [24, 38, 13]
})
print(f"Average Price : {sum(df_fruit['가격']) / df_fruit['가격'].size}")
print(f"Average Solved Price : {sum(df_fruit['판매량']) / df_fruit['판매량'].size}")

# Excel 파일 읽기
df_excel = pd.read_excel('./excel_exam.xlsx')
print(df_excel)
print(f"Exel eng Average grade : {sum(df_excel['english']) / df_excel['english'].size}")

# CSV(Comma Seperated Values) 파일 읽기
df_csv = pd.read_csv('./exam.csv')
print(df_csv)

# 데이터 프레임을 CSV 파일로 저장하기
df_fruit.to_csv('FruitDataFrame.csv', index=False)