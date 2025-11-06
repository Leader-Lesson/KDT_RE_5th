import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.__version__

plt.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'이 설치되어 있을 경우
plt.rcParams['axes.unicode_minus'] = False     # 마이너스(-) 부호 깨짐 방지

x = [1,2,3,4,5]
y = [10,13,17,19,24]

# 선 그래프
plt.plot(x,y)

# 이미지를 파일로 저장
plt.savefig("my_graph.png")

# 콘솔에 이미지 그리기
plt.show()

# subplots()
# fig, axs = plt.subplots(행, 열)
fig, axs = plt.subplots() # 하나의 figure와 하나의 axes를 만듦

# 1행 2열의 axes 생성
fig, axs = plt.subplots(1,2)

axs[0].plot([1,2,3], [1,2,3])
axs[1].plot([1,2,3], [1,4,9])

plt.show()

# 2행 2열의 axes 생성
fig, axs = plt.subplots(2, 2)

fig.suptitle("여러 함수 그래프")

axs[0, 0].plot([1,2,3], [1,2,3])
axs[0, 0].set_title("1번 그래프")

axs[0, 1].plot([1,2,3], [1,4,9])
axs[0, 1].set_title("2번 그래프")

axs[1, 0].plot([1,2,3], [3,2,1])
axs[1, 0].set_title("3번 그래프")

axs[1, 1].plot([1,2,3], [9,4,1])
axs[1, 1].set_title("4번 그래프")

plt.tight_layout() # 그래프 간격 자동 조정

plt.show()

# title - 기본
plt.plot([1,2,3,4,5], [1,4,9,16,25], 
        label="제곱 그래프",
        linestyle="--",
        color="c",
        marker="o")
plt.title("제곱 함수 그래프", color="b", fontsize=20)

# xlabel, ylabel - 기본
plt.xlabel("x 값")
plt.ylabel("y 값(x의 제곱)")

# xticks, yticks
plt.xticks([1,2,3,4,5],["A","B","C","D","E"])
plt.yticks([1,5,10,15,20])

# 범례(legend)
plt.legend()

# 격자(grid)
plt.grid(linestyle="--")

plt.show()

# title - subplot
fig, axs = plt.subplots()

axs.plot([1,2,3],[1,4,9], "bo--", label="제곱그래프")
axs.set_title("제곱 함수 그래프")

# x라벨, y라벨 - subplot
axs.set_xlabel("x값")
axs.set_ylabel("y값(x의 제곱)")

# 범례(legend)
axs.legend()

# 격자(grid)
axs.grid()

plt.show()

# 하나의 axes에 여러개의 그래프 그리기
x = np.arange(0,10)
y1 = 2 * x + 1
y2 = 3 * x - 5

plt.plot(x, y1, marker="o", label="y = 2x + 1", color="c")
plt.plot(x, y2, marker="*", label="y = 3x - 5", color="m")

plt.title("두개의 선 그래프 비교")
plt.xlabel("x값")
plt.ylabel("y값")
plt.legend()
plt.grid(linestyle=":", alpha=0.5)

plt.show()

# 실습1. 선 그래프 그리기
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2019 = [100,120,140,110,130,150,160,170,180,200,190,210]
sales_2020 = [90,110,130,120,140,160,170,160,150,180,200,190]

plt.plot(sales_2019, label="2019 판매량", linestyle="--", marker="o")
plt.plot(sales_2020, label="2020 판매량", linestyle="--", marker="^")

plt.xlabel("월", labelpad=15)
plt.ylabel("판매량", labelpad=15)

x = np.arange(12)
plt.xticks(x, months)

plt.title("Monthly sales comparison(2019-2020)")
plt.grid(linestyle=":", alpha=0.5)
plt.legend(loc="lower right", title="판매 연도")

plt.show()

# 막대 그래프
labels = ["A","B","C","D"]
values = [10, 24, 15, 32]

plt.bar(labels, values)

plt.show()

# 수평 막대 그래프
plt.barh(labels, values)
plt.show()

# 여러 막대그래프
labels = ["1분기","2분기","3분기","4분기"]
men_means = [20, 34, 30, 35]
women_means = [25, 32, 34, 40]

x = np.arange(len(labels))

fig, ax = plt.subplots()
width = 0.4

ax.bar(x - width/2, men_means, width, label="남성")
ax.bar(x + width/2, women_means, width, label="여성")

ax.set_xticks(x, labels)

plt.show()

# 실습2. 막대그래프
categories = ['Category 1','Category 2','Category 3','Category 4','Category 5']
data = [20, 35, 15, 27, 45]

plt.bar(categories, data)

plt.title("Bar Chart")
plt.grid(linestyle=":")

plt.xlabel("Categories")
plt.ylabel("Values")

plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.ylim(0, 50)

plt.show()

# 히스토그램
# 랜덤 데이터 생성
data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor="k")

plt.show()

# 실습3.
np.random.seed(42) # 난수의 초기값 지정
dice = np.random.randint(1, 7, 100)

cnt, bins, _ = plt.hist(dice, bins=np.arange(1,8)-0.5, edgecolor="k", rwidth=0.8)
print(bins)

plt.show()

# 산점도
# x = [5, 7, 8, 10, 12]
# y = [20, 25, 15, 30, 22]
x = np.linspace(2, 30, 20)
y = np.linspace(10, 40, 20)
y_noisy = y + np.random.uniform(-7, 7, 20) # uniform 지정한 구간안에서 실수 난수

plt.scatter(x, y_noisy)
plt.grid(linestyle=":")

plt.show()

labels = ['Apple', 'Banana', 'Mango', 'Blueberry']
sizes = [15,30,45,10]
explode = (0,0.1,0,0)

plt.pie(sizes, labels=labels, explode=explode, shadow=True, autopct="%1.1f%%",
        startangle=90, colors=["#a6e3ff","#a6ffad", "#ffa6c3", "#ff804a"])

plt.show()