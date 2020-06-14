import pandas as pd
import numpy as np
from numpy import nan as NA
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header = None)

# 각각의 수치가 나타내는 바를 컬럼에 추가합니다
df.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash",
            "Magnesium", "Total phenols", "Flavanoids",
            "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue",
            "OD280/OD315 of diluted wines","Proline"]

# 변수 df의 상위 10행을 변수 df_ten에 대입하여 표시하세요
df_ten = df.head(10)
print(df_ten)

# 데이터의 일부를 누락시킵니다
df_ten.iloc[1,0] = NA
df_ten.iloc[2,3] = NA
df_ten.iloc[4,8] = NA
df_ten.iloc[7,3] = NA
print(df_ten)

# fillna() 메서드로 NaN 부분에 열의 평균값을 대입하세요
df_ten.fillna(df_ten.mean())
print(df_ten)

# "Alcohol" 열의 평균을 출력하세요
print(df_ten["Alcohol"].mean())

# 중복된 행을 제거하세요
df_ten.append(df_ten.loc[3])
df_ten.append(df_ten.loc[6])
df_ten.append(df_ten.loc[9])
df_ten = df_ten.drop_duplicates()
print(df_ten)

# Alcohol 열의 구간 리스트를 작성하세요
alcohol_bins = [0,5,10,15,20,25]
alcoholr_cut_data = pd.cut(df_ten["Alcohol"],alcohol_bins)

# 구간 수를 집계하여 출력하세요
print(pd.value_counts(alcoholr_cut_data))
