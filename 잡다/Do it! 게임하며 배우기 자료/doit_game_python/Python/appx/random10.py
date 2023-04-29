# 무작위 숫자 10개 만들기

# 라이브러리 불러오기
import random

# 결과를 저장할 리스트 초기화하기
numbers = []

# 숫자 10개를 얻을 때까지 루프 반복하기
while numbers.count(10) < 10:
    # 무작위 숫자 만들기
    num = random.randrange(1, 101)
    # 이미 만든 숫자인지?
    if not num in numbers:
        # 아니요, 리스트에 추가하기
        numbers.append(num)

# 숫자 출력하기
print(numbers)