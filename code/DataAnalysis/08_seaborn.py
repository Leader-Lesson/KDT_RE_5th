import seaborn as sns
import matplotlib.pyplot as plt

sns.__version__

# 사용 가능한 데이터셋 이름 출력
sns.get_dataset_names()

# 데이터셋 로드
df = sns.load_dataset("diamonds")
df.head(10)

import matplotlib.font_manager as fm

for f in fm.fontManager.ttflist :
  print(f.name)

# 방법1.
sns.set_style("ticks")
sns.set_context("notebook")
sns.set_palette("pastel")
plt.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'이 설치되어 있을 경우
plt.rcParams['axes.unicode_minus'] = False     # 마이너스(-) 부호 깨짐 방지

# 방법2
# sns.set_theme(
#   style="whitegrid",
#   rc={
#     "font.family": "Malgun Gothic",
#     "axes.unicode_minus": False
#   }
# )

# 범주형 데이터 그래프
# countplot
palette = sns.color_palette("pastel")
tips = sns.load_dataset("tips")
sns.countplot(data=tips, x="day", hue="sex", palette=palette)
plt.title("요일별 방문자수")
plt.grid(linestyle=":")
plt.show()

# barplot
palette = sns.color_palette("colorblind")
sns.barplot(data=tips, x="day", y="tip", palette=palette)
plt.title("요일별 평균 팁 금액")
plt.show()

# displot()
# 히스토그램 + 커널 밀도(kde)
# kde=True로 하면 kde 그래프그려줌
# sns.displot(data=tips, x="total_bill", bins=20)
sns.displot(data=tips, x="total_bill", kde=True, bins=20)
plt.title("Total bill")
plt.show()

# scatterplot()
# 산점도
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.show()

# heatmap()
# 상관계수행렬의 그래프
penguins = sns.load_dataset("penguins")

# 상관계수행렬
corr = penguins.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="inferno")
plt.show()

# jointplot()
sns.jointplot(data=penguins, x="flipper_length_mm", y="body_mass_g", kind="scatter")
plt.show()