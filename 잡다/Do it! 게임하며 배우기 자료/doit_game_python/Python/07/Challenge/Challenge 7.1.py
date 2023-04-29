# 숫자 맞히기 게임 만들기 추가적용(최대값,최소값 입력, 입력한 횟수, 최대값이나 최소값보다 크거나 작으면 경고문 추가)
import random

Attempt = 0
raMin = 1
raMax = 100
uinput = ''
unumber = 0

raNnumber = random.randrange(raMin, raMax + 1)

uinput = print('숫자 맞추기 게임을 하겠습니다', raMin, '과', raMax, '중 하나를 맞춰보세요!')
while raNnumber != unumber:
    uinput = input('예상 숫자를 입력해주세요:').strip()
    if not uinput.isnumeric():
        print('숫자가 아닙니다.')
    elif raNnumber < raMin or raNnumber > raMax:
        print(uinput, '은', raMin, '과', raMax, '에 사이가 아닙니다.')
    else:
        unumber = int(uinput)
        Attempt = Attempt + 1
        if raNnumber > unumber:
            print('숫자가 더 큽니다.')
            if raNnumber > unumber + 15:
                print('휠씬 더 큰 숫자를 입력하세요.')
        elif raNnumber < unumber:
            print('숫자가 더 작습니다.')
            if raNnumber < unumber - 15:
                print('훨씬 더 작은 숫자를 입력하세요.')
        else:
            print(f'정답입니다! 정답은 {raNnumber}입니다. 시도 횟수: {Attempt}')
