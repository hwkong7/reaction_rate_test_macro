import webbrowser
import time
import pyautogui

# 1️⃣ 반응속도 테스트 사이트 열기
url = "https://hwkong7.github.io/reaction_rate_test_macro/button_click"
webbrowser.open(url)   # 기본 브라우저로 열기

# 2️⃣ 브라우저 로딩 시간 대기
#time.sleep(5)  

# 3️⃣ 대기 후 자동 클릭 로직 실행
x, y = 1430, 754  # 초록 버튼 중앙 좌표 
print("🎯 초록색 감지 대기 중...")

while True:
    color = pyautogui.pixel(x, y)
    if 50 < color[1] and color[0] < 100 and color[2] < 100: # 초록색 감지 조건
        pyautogui.click(x, y)
        print("✅ 초록색 감지 즉시 클릭!")
        #break
    #time.sleep(0.001)
