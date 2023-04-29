# 라이브러리 불러오기
import random
 
# 변수 초기화하기
maxLives = 7        # 최대 시도 횟수
maskChar = "_"      # 마스킹 문자
livesUsed = 0       # 시도 횟수
guessedLetters = [] # 추측한 문자 저장
wordLetters = []    # 단어에 포함된 모든 문자
victory = False     # 단어를 맞히면 True가 됨
 
# 게임 단어
gameWords = ["anvil", "boutique", "cookie", "fluff",
            "jazz", "pneumonia", "sleigh", "society",
            "topaz", "tsunami", "yummy", "zombie",
            "rhythm"]
 
# 게임에 사용할 단어 고르기
gameWord = random.choice(gameWords)
 
# 단어에 포함된 모든 문자 가져오기
for letter in gameWord:
    # 리스트에 이 문자가 없는지 확인하기
    letterInList = False
    # 문자를 대상으로 루프
    for wl in wordLetters:
        # 각 문자 확인하기
        if wl == letter:
            # 문자가 있다면
            letterInList = True
    # 문자가 없다면
    if not letterInList:
        # 이 문자를 리스트에 추가하기
        wordLetters.append(letter)
# 리스트 정렬하기
wordLetters.sort()
 
# 게임 시작하기
# 최대 시도 횟수가 되거나 단어를 맞힐 때까지 루프
while livesUsed < maxLives and victory == False:
 
    # 먼저 단어 마스킹하기
    # 빈 문자열로 시작하기
    displayWord = ""
    # 1자씩 루프하기
    for letter in gameWord:
         # 추측한 문자가 맞는지?
         if letter in guessedLetters:
             # 맞힌 문자이므로 출력할 문자열에 추가하기
             displayWord += letter
         else:
             # 아직 맞히지 않은 문자는 마스킹하기
             displayWord += maskChar
    # 마스킹한 단어 출력하기
    print(displayWord)
 
    # 다음으로 이미 추측한 문자 표시하기
    # 추측한 문자가 있는지?
    if len(guessedLetters) > 0:
        # 입력한 내용이 있다면 빈 문자열로 시작하기
        youTried = ""
        # 추측한 문자 모두 더하기
        for letter in guessedLetters:
            youTried += letter
        # 출력하기
        print("시도한 문자:", youTried)
    
    # 추측 문자 입력받기
    currGuess = ""
    # 1자만 입력받기
    while len(currGuess) != 1:
        currGuess = input("추측 문자:").lower()
 
    # 같은 문자 반복 추측 방지하기
    if currGuess in guessedLetters:
        print("이미 추측한 문자입니다.", currGuess)
    # 반복 문자가 아니라면
    else:
        # 추측 문자 리스트에 저장하기
        guessedLetters.append(currGuess)
        # 정렬하기
        guessedLetters.sort()
        
        # 올바른 추측인가요?
        if currGuess in gameWord:
            # 정답이라면
            print ("올바른 추측입니다.")
            # 이 문자를 추측했으므로
            # 단어 문자에서 이를 삭제
            wordLetters.remove(currGuess)
        else:
            # 정답이 아니라면
            print ("틀렸습니다.")
            # 시도한 횟수 하나 늘리기
            livesUsed += 1
    
    # 보기 좋게 빈 줄 출력하기
    print()
 
    # 사용자가 이겼는지 확인하기(추측 문자가 없음)
    if len(wordLetters) == 0:
        # 이겼다면
        victory = True
    else:
        # 남은 시도 횟수 출력하기
        print (maxLives - livesUsed, "번 남았습니다.")
 
# 게임을 끝내고 결과 출력하기
if victory:
    # 이겼다면
    print ("여러분이 이겼습니다. 단어는", gameWord, "입니다!")
else: 
    # 졌다면
    print ("여러분이 졌습니다. 정답:", gameWord)
