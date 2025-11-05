import folium

m = folium.Map(location=[37.61119807384533, 126.91731049700418],
              zoom_start=18)

# 기본 마커
folium.Marker([37.61119807384533, 126.91731049700418],
              popup="Subway",
              tooltip="구산역",
              icon=folium.Icon(color="black", icon="fa-solid fa-bus", prefix="fa-solid")
              ).add_to(m)

# 원형 마커
folium.CircleMarker(
  [37.61020411781574, 126.9133136519163],
  radius=100,
  color="#adcdff",
  fill_color ="#1c73ff",
  popup="CircleMarker",
  tooltip="tooltip"
).add_to(m)

# 클릭한 곳에 마커 추가
m.add_child(folium.ClickForMarker(popup="내가 클릭한 곳"))

# 클릭한 곳의 위도와 경도 표시
m.add_child(folium.LatLngPopup())

m

# 실습2.
import folium
import pandas as pd

df = pd.read_csv("dataset/택시승차대 현황.csv", encoding="CP949")

taxi = df.loc[:, ["위치명","위도","경도"]]
latitude = taxi["위도"].mean()
longitude = taxi["경도"].mean()
m = folium.Map([latitude, longitude], zoom_start=13)

for idx, row in taxi.iterrows():
  # print(idx, row["위치명"], row["위도"], row["경도"])
  folium.Marker(
    [row["위도"],row["경도"]],
    tooltip = row["위치명"],
    icon=folium.Icon(color="orange", icon="fa-solid fa-taxi", prefix="fa-solid")
  ).add_to(m)

m