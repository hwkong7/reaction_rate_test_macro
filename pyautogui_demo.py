import cv2
import pyautogui
import time

# 0️⃣ 실행 준비
print("3초 후 자동 제어를 시작합니다! 준비하세요 😎")
#time.sleep(3)

# # 1️⃣ 마우스 이동
# print("1️⃣ 마우스를 (500, 400) 위치로 1초 동안 이동합니다.")
# pyautogui.moveTo(500, 400, duration=1)
# time.sleep(1)

# # 2️⃣ 마우스 클릭
# print("2️⃣ 마우스를 클릭합니다.")
# pyautogui.click()
# time.sleep(1)

# # 3️⃣ 키보드 입력
# print("3️⃣ 문자를 자동으로 입력합니다. (입력창에 커서를 두세요!)")
# pyautogui.write("Hello pyautogui!", interval=0.1)
# time.sleep(1)

# # 4️⃣ 핫키 조합 (Ctrl + S)
# print("4️⃣ Ctrl + S 단축키를 눌러봅니다.")
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)

# # 5️⃣ 스크린샷
# print("5️⃣ 스크린샷을 찍어서 capture.png로 저장합니다.")
# screenshot = pyautogui.screenshot()
# screenshot.save("capture.png")
# print("📸 capture.png 저장 완료!")
# time.sleep(1)

# 6️⃣ 화면 인식 (이미지 찾기 예시)
print("3초 후 화면에서 button_green.png를 찾습니다...")
time.sleep(0)

# loc = pyautogui.locateOnScreen('button_green.png', confidence=0.7, grayscale=False)
# if loc:
#     print("✅ 찾음:", loc)
#     pyautogui.moveTo(pyautogui.center(loc))
#     pyautogui.click()
# else:
#     print("❌ 화면에서 못 찾음.")
    
    

# if loc:
#     print("✅ 찾음:", loc)
#     # 버튼 중심 좌표 계산
#     x, y = pyautogui.center(loc)

#     # moveTo(duration=0) 으로 즉시 이동 후 click
#     pyautogui.moveTo(x, y, duration=0)  # 즉시 이동
#     pyautogui.mouseDown()               # 눌렀다
#     pyautogui.mouseUp()                 # 바로 뗌 (click보다 빠름)
#     print("⚡ 즉시 클릭 완료!")
# else:
#     print("❌ 화면에서 못 찾음.")


# x, y = pyautogui.position()
# print(f"📍 현재 좌표: ({x}, {y})")

x, y = 1430, 754  # 버튼 중앙 위치
while True:
    color = pyautogui.pixel(x, y)
    if 50 < color[1] and color[0] < 100 and color[2] < 100: # 초록색 감지 조건
        pyautogui.click(x, y)
        print("✅ 초록색 감지 즉시 클릭!")
        break

#pyautogui.alert("자동 제어를 종료.","제목")

#name = pyautogui.prompt('이름을 입력하세요:',"제목")