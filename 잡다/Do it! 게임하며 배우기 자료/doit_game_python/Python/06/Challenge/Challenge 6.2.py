# 사용할 아스키 범위 - 이 범위를 벗어나면 오류가 발생합니다.
asciiMin = 32   # 공백 문자를 나타냄 - " "
asciiMax = 126  # 물결표 문자를 나타냄 - "~"
 
# 암호화 키
key = 314159    # 일급비밀! 이것이 암호화 키입니다.
key = str(key)  # 각 문자에 접근할 수 있도록 문자열로 변환하기

# 암호화인지 복호화인지 정하기
action = input("암호화(E) 또는 복호화(D)? 대문자 E 또는 D를 입력하세요: ")

# 메시지 입력받기(암호화할 메시지 또는 복호화할 메시지)
if action == 'E':
    message = input("암호화할 메시지를 입력하세요: ")
elif action == 'D':
    message = input("복호화할 메시지를 입력하세요: ")
 
# 암호화 메시지용 변수 초기화하기
messEncr = ""

# E나 D를 입력했을 때만 루프 반복하기
if action in ['D', 'E']: 
    # 메시지 루프
    for index in range(0, len(message)):
        # 해당 문자의 아스키값 가져오기
        char = ord(message[index])
        # 이 문자가 범위 밖에 있는지?
        if char < asciiMin or char > asciiMax:
            # 예, 암호화에 적당하지 않으므로 그대로 둡니다.
            messEncr += message[index]
        else:
            # 이 문자를 암호화하거나 복호화해도 안전합니다.
            if action == 'E':
                # 키만큼 값을 더하여 암호화합니다.
                ascNum = char + int(key[index % len(key)])
                # 더한 값이 범위를 벗어난다면 범위 처음으로 되돌립니다.
                if ascNum > asciiMax:
                    ascNum -= (asciiMax - asciiMin)
            elif action == 'D':
                # 키만큼 값을 빼서 복호화합니다.
                ascNum = char - int(key[index % len(key)])
                # 옮긴 값이 범위를 벗어난다면 범위 끝으로 되돌립니다.
                if ascNum < asciiMin:
                    ascNum += (asciiMax - asciiMin)
            # 문자로 변환하고 출력할 내용에 추가합니다.
            messEncr = messEncr + chr(ascNum)
    
    # 결과 출력하기
    print("암호화한 메시지: ", messEncr)
else:
    print("대문자 E 또는 D만 입력해야 합니다.")