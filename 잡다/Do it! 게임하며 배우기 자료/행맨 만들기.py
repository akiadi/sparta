from random import choice

# 변수 초기화하기
maxLives = 7  # 최대 허용 추측 횟수
maskChr = '_'  # 마스킹 문자
livesUsed = 0  # 시도 횟수
user_guess = []  # 사용자 추측 문자를 저장할 리스트

gamewords = ['강아지', '호랑이', '하마', '사슴', '바다사자', '사자', '여우', '고양이', '코끼리', '치타', '낙타', '기린']

gameword = choice(gamewords)

displayword = maskChr * len(gameword)

while gameword != displayword and livesUsed < maxLives:
    print(displayword)
    if len(user_guess) > 0:
        youTried = ""
        for letter in user_guess:
            youTried += letter
        print('시도한 문자:', youTried)
    print(maxLives - livesUsed, "번 남았습니다.")
    print()

    currGuess = input('추측문자:').strip().lower()
    if len(currGuess) > 1:
        currGuess = currGuess[0]
    if currGuess in user_guess:
        print('이미 추측한 문자입니다:', currGuess)
    else:
        user_guess.append(currGuess)
        user_guess.sort()

        displayword = ''
        for letter in gameword:
            if letter in user_guess:
                displayword += letter
            else:
                displayword += maskChr

        if currGuess in gameword:
            print('올바른 추측입니다.')
        else:
            print('틀렸습니다.')
            livesUsed += 1
        print()

if displayword == gameword:
    print('여러분이 이겼습니다.')
else:
    print('여러분이 졌습니다.')
