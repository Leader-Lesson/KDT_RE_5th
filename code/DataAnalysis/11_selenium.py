from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time

# Chrome 브라우저 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 원하는 페이지로 이동
driver.get("https://www.google.com")
time.sleep(3)
driver.get("https://www.naver.com")
time.sleep(3)

# 페이지 이동
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(1)

# 크기변경
driver.set_window_size(1200, 800)
time.sleep(2)

# 최대화
driver.maximize_window()
time.sleep(2)

# 최소화
driver.minimize_window()
time.sleep(2)

# 창 배치
driver.set_window_position(50, 50)

# 스크린샷 찍기
driver.save_screenshot("naver.png")

time.sleep(3)
driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 웹페이지의 요소 선택과 제어
text_input = driver.find_element(By.ID, "my-text-id")

time.sleep(5)

# 요소 제어
text_input.send_keys("Hello Selenium!!")
time.sleep(3)
text_input.clear()
time.sleep(3)
text_input.send_keys("코딩은 재밌어ㅋㅋ")
time.sleep(3)
# text_input.send_keys(Keys.RETURN)

submit_btn = driver.find_element(By.TAG_NAME, "button")
submit_btn.click()

msg = driver.find_element(By.ID, "message")
print("제출 결과:", msg)
print("제출 내용:", msg.text)

time.sleep(5)
driver.quit()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

time.sleep(3)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python", Keys.RETURN)

time.sleep(10)

driver.quit()