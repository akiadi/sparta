import tkinter as tk
import subprocess
import pyautogui
import time
import webbrowser
# 사이트 로그인 무조건 되있어야 합니다
def run_code():
    time.sleep(0.5)     # 주소 코드도 바꾸기!
    url = "https://www.dpsnnn.com/reserve/?idx=36&day=2023-04-19"
    webbrowser.open(url)

    time.sleep(0.5)
# 예약하기 클릭
    pyautogui.moveTo(1225, 879, duration=0.3)
    pyautogui.click()
# -500 내리고
    time.sleep(1)
    pyautogui.scroll(-500)
    time.sleep(1)
# 이용자 전화번호 클릭
    pyautogui.moveTo(979, 384, duration=0.05)
    pyautogui.click()
# 이용자 전화번호 입력
    pyautogui.typewrite('01031019188\n')

# 2인 클릭
    pyautogui.moveTo(590, 626, duration=0.05)
    pyautogui.click()
# 동의하기
    pyautogui.moveTo(582, 1007, duration=0.05)
    pyautogui.click()
#전체 동의하기
    pyautogui.moveTo(1119, 702, duration=0.05)
    pyautogui.click()

#결제하기   !!!! 실제 사용시 pyautogui.click() 추가하기
    pyautogui.moveTo(1254, 795, duration=0.05)

# 윈도우 생성
window = tk.Tk()
window.title("단편선")

# 창 크기 설정
window.geometry("300x100")

# 버튼 생성
button = tk.Button(text="클릭", command=run_code)
button.pack()

# 윈도우 실행
window.mainloop()