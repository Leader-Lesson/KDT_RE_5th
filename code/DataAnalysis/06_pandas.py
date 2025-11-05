import pandas as pd

# csv 파일 불러오기
df = pd.read_csv("practice_book_dataset.csv")
df.head()

# 데이터 정보 확인
df.shape
df.dtypes
df.info()
df.describe()

df["title"].head(10)
df[["title","author"]].head(10)

df2 = df.copy()
df2["libarary"] = "seoul library"
df2.to_csv("new_book_dataset.csv")

mask = df["price"] >= 100
df[mask]
df.loc[mask, ["title", "price", "avg_reviews"]]

df.isnull().sum()

# excel 파일 불러오기
df = pd.read_excel("practice_employee_dataset.xlsx")
df.head()

# excel(xlsx) 파일로 저장
df2 = df.copy()
df2["Working Period"] = 3
df2.head(10)
df.to_excel("New_employee_dataset.xlsx")

df = pd.read_csv("dataset/dataset.csv")
df.describe()
df.info()

df = pd.read_excel("dataset/dataset2.xlsx")
df