# 라이브러리 불러오기
import random

# 사용자에게 이름 묻기
cheat = input("가위바위보를 해볼까요? 시작하려면 'start'라고 적어주세요: ")

# 컴퓨터가 선택하기
cChoice = random.choice("SRP")
 
# 사용자 선택 입력받기
uChoice = input("S(가위), R(바위), P(보) 중 하나를 고르세요: ").upper().strip()

# 일급비밀 코드 - 나만의 비밀로 만들기! 
# ('$'를 붙이고 앞뒤에 공백 추가)
if cheat == "start1":
    if uChoice == "R":
        cChoice = "S"
    elif uChoice == "P":
        cChoice = "R"
    elif uChoice == "S":
        cChoice = "P"

# 선택 비교하기
if cChoice == uChoice:
    print("무승부입니다!")
elif uChoice == "R" and cChoice == "P":
    print("여러분이 고른 것은 바위(R), 컴퓨터가 고른 것은 보(P). 여러분이 졌네요.")
elif uChoice == "P" and cChoice == "R":
    print("여러분이 고른 것은 보(P), 컴퓨터가 고른 것은 바위(R). 여러분이 이겼네요.")
elif uChoice == "R" and cChoice == "S":
    print("여러분이 고른 것은 바위(R), 컴퓨터가 고른 것은 가위(S). 여러분이 이겼네요.")
elif uChoice == "S" and cChoice == "R":
    print("여러분이 고른 것은 가위(S), 컴퓨터가 고른 것은 바위(R). 여러분이 졌네요.")
elif uChoice == "P" and cChoice == "S":
    print("여러분이 고른 것은 보(P), 컴퓨터가 고른 것은 가위(S). 여러분이 졌네요.")
elif uChoice == "S" and cChoice == "P":
    print("여러분이 고른 것은 가위(S), 컴퓨터가 고른 것은 보(P). 여러분이 이겼네요.")
else:
    print("게임 설명을 또 듣는 일은 지겨울 겁니다. 그렇죠?")