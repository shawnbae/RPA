import pyautogui
#pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
pyautogui.mouseInfo() # 마우스 정보 열

for i in range(5):
    pyautogui.move(100, 100)