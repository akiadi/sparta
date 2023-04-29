# 음식값을 알아야한다
# 팁을 계산한 후, 변수에 저장하는것이 필요
# 음식값, 팁, 음식값과 팁을 합한 지불할 금액등 모든정보를 출력
# 서비스 평점에따라 팁 비율을 정하는방식과 사람 수를 입력받아 더치페이를 할수있게 만들어봅시다  / 반올림 round()

#음식값 계산기 만들기 더치페이도 함께 되는 계산기를 만들껀데 사용자 정의 함수를 사용하여 만들기.

def food_name(txt):
    line = '-'
    line2 = '*'
    print(line * (len(txt) + 4))
    print(line2, txt, line2)
    print(line * (len(txt) + 4))
    return

def food_cost():
    uinput = ''
    while not uinput.isnumeric():
        uinput = input('음식값을 입력하세요:').strip()
    return int(uinput)


txt = input('음식 이름을 입력하세요: ')
money = food_cost()
tip_rate = input('서비스가 어땠는지 평을 매겨보세요(1 ~ 5점) 예시) 5점: ').strip()
total_tip_food = 0

if tip_rate == '1점':
    total_tip_food = money
elif tip_rate == '2점':
    total_tip_food = money + (money * 0.25)
elif tip_rate == '3점':
    total_tip_food = money + (money * 0.50)
elif tip_rate == '4점':
    total_tip_food = money + (money * 0.75)
elif tip_rate == '5점':
    total_tip_food = money + (money * 1.00)

Dutch_Pay = int(input('더치페이 할 총인원을 적어주세요 없다면 1을 입력하세요: '))
total_value = 0
ndutch = Dutch_Pay
if Dutch_Pay == 1:
    total_value = total_tip_food
elif Dutch_Pay == ndutch:
    total_value = round(total_tip_food / ndutch, 1)

food_name(txt)
print(f'음식값: {money}\n서비스 평가: {tip_rate}\n더치페이: {Dutch_Pay}\n총합계: {total_value}')