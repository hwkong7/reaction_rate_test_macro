import webbrowser
import time
import pyautogui

# 1️⃣ 반응속도 테스트 사이트 열기
url = "https://www.arealme.com/reaction-test/ko/"
webbrowser.open(url)   # 기본 브라우저로 열기

# 2️⃣ 브라우저 로딩 시간 대기
time.sleep(5)  # (초 단위, 필요하면 늘려도 돼)

# 3️⃣ 대기 후 자동 클릭 로직 실행
x, y = 1430, 754  # 초록 버튼 중앙 좌표 (화면에 맞게 조정!)
print("🎯 초록색 감지 대기 중...")

while True:
    color = pyautogui.pixel(x, y)
    if color[1] > 150 and color[0] < 100 and color[2] < 150:
        pyautogui.click(x, y)
        print("✅ 초록색 감지 즉시 클릭!")
        break
    time.sleep(0.001)
