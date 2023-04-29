import tkinter as tk
import subprocess

def run_code():
    # 실행할 코드가 들어갈 부분입니다.
    code = "print('Hello, world!')"
    subprocess.call(['python', '-c', code])

# 윈도우 생성
window = tk.Tk()
window.title("사용자 정의 제목")
# 창 크기 설정
window.geometry("300x100")

# 버튼 생성
button = tk.Button(text="Run Code", command=run_code)
button.pack()

# 윈도우 실행
window.mainloop()
