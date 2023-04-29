import pyautogui
import time
import webbrowser

"""time.sleep(1)
url = "https://www.dpsnnn.com/reserve/?idx=34&day=2023-04-20"
webbrowser.open(url)"""
# 스크롤 내리기
time.sleep(1)
pyautogui.scroll(-2000)

# 마우스 위치
time.sleep(3)
print(pyautogui.position())


"""
# 마우스 위치 클릭
pyautogui.moveTo(979, 384, duration=0.05)
pyautogui.click()

# 키보드 타자
pyautogui.typewrite('01024283402\n')
"""
"""    pyautogui.moveTo(1200, 920, duration=0.8)
    pyautogui.click()"""
