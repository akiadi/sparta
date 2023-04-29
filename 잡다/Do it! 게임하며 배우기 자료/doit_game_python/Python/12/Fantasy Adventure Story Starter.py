##########################################
# 판타지 어드벤처
# 벤 & 쉬무엘 만듦
##########################################
 
# 플레이어 환영 메시지
def doWelcome():
    # 텍스트 출력하기
    print("탐험가 여러분을 환영합니다!")
 
# 위치: 숲속 빈터
def doClearing():
    # 텍스트 출력하기
    print("여러분은 버려진 숲 속 빈터에 있습니다.")
    print("숲 속으로 들어가는 오래된 길이 여러분 앞에 있습니다.")
    print("오른쪽으로 시선을 돌리니 동쪽 풍경은 키 높은 식물에 가려 잘 보이지 않습니다.")
    print("서쪽 어디선가 부석거리는 소리가 들립니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "NEW":
        print("무엇을 하시겠습니까?:")
        print("N = 북쪽으로 간다")
        print("E = 동쪽으로 간다")
        print("W = 서쪽으로 간다")
        choice = input("무엇을 하시겠습니까? [N/E/W]").strip().upper()
    # 행동 수행하기
    if choice == 'N':
        doWoods1()
    elif choice == 'E':
        doVegetationEast()
    elif choice == 'W':
        doCampSite()

# 위치: 동쪽으로 향하는 숲 속
def doVegetationEast():
    # 텍스트 출력하기
    print("우거진 숲 속으로 천천히 걸어갑니다.")
    print("천천히, 천천히.")
    print("마침내 숲을 나와 바위 지역으로 난 길을 발견합니다.")
    print("동쪽으로 흐르는 물소리가 들립니다.")
    print("숲 속 빈터는 여러분이 온 서쪽에 있습니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "EWR":
        print("무엇을 하시겠습니까?:")
        print("E = 동쪽으로 간다")
        print("W = 서쪽으로 간다")
        print("R = 암벽을 조사한다")
        choice = input("무엇을 하시겠습니까? [E/W/R]").strip().upper()
    # 행동 수행하기
    if choice == 'E':
        doRiver()
    elif choice == 'W':
        doClearing()
    elif choice == 'R':
        doRocks()

# 위치: 바위 길
def doRocks():
    # 텍스트 출력하기
    print("암벽 위를 살펴봅니다. 바위틈이 보입니다.")
    print("동쪽으로 흐르는 물소리가 더 크게 들립니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "EWC":
        print("무엇을 하시겠습니까?:")
        print("E = 동쪽으로 간다")
        print("W = 서쪽으로 간다")
        print("C = 바위틈을 조사한다")
        choice = input("무엇을 하시겠습니까? [E/W/C]").strip().upper()
    # 행동 수행하기
    if choice == 'E':
        doRiver()
    elif choice == 'W':
        doClearing()
    elif choice == 'C':
        doCrevice()

# 위치: 바위틈
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 바위틈에 검이 있다.
# 거미줄을 없애려면 횃불이 필요하다.
def doCrevice():
    # 텍스트 출력하기
    print("바위틈은 거미줄 같은 것으로 막혔습니다.")
    print("이렇게 크고 두꺼운 거미줄을 만드는 거미는 얼마나 클까 놀랍습니다.")
    print("안타깝게도 거미줄을 찢고 들어갈 수는 없습니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "B":
        print("무엇을 하시겠습니까?:")
        print("B = 되돌아간다")
        choice = input("무엇을 하시겠습니까? [B]").strip().upper()
    # 행동 수행하기
    if choice == 'B':
        doRocks()

# 위치: 강
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 강을 건널 수 있는지?
# 다리를 고치는 등 다른 선택은?
def doRiver():
    # 텍스트 출력하기
    print("물소리가 들리는 쪽으로 걸어갑니다. 그리곤 바로 멈춥니다!")
    print("벼랑 끝입니다. 사나운 물소리는 그 벼랑 아래 강에서 들려옵니다.")
    print("다행스럽게도 강을 건너는 다리가 보입니다.")
    print("그러나 다리 대부분은 부서졌으며 강 아래에 잠겼습니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "W":
        print("무엇을 하시겠습니까?:")
        print("W = 서쪽으로 간다")
        choice = input("무엇을 하시겠습니까? [W]").strip().upper()
    # 행동 수행하기
    if choice == 'W':
        doRocks()

# 위치: 캠프장
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 플레이어에게 나뭇가지가 있다면 불씨를 이용하여 불을 붙일 수 있도록 하기
def doCampSite():
    # 텍스트 출력하기
    print("이곳은 캠프장인 듯합니다.")
    print("아무도 없으나 불씨를 보니 얼마 전까지 누군가가 있었던 듯합니다.")
    print("숲 속 빈터는 동쪽에 있습니다.")
    print("북쪽을 보니 캄캄한 숲이 보입니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "NE":
        print("무엇을 하시겠습니까?:")
        print("N = 북쪽으로 간다")
        print("E = 동쪽으로 간다")
        choice = input("무엇을 하시겠습니까? [N/E]").strip().upper()
    # 행동 수행하기
    if choice == 'N':
        doForest1()
    elif choice == 'E':
        doClearing()

# 위치: 숲1
def doForest1():
    # 텍스트 출력하기
    print("아무것도 보이지 않은 숲 속입니다. 오래 머물러서는 안 될 듯합니다.")
    print("캠프장은 남쪽에 있습니다.")
    print("동쪽, 서쪽, 북쪽으로 서성거려 봅니다.")
    print("그러나 아무것도 볼 수 없습니다. 남쪽으로 가는 것이 좋을 듯합니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "NSEW":
        print("무엇을 하시겠습니까?:")
        print("N = 북쪽으로 간다")
        print("S = 남쪽으로 간다")
        print("E = 동쪽으로 간다")
        print("W = 서쪽으로 간다")
        choice = input("무엇을 하시겠습니까? [N/S/E/W]").strip().upper()
    # 행동 수행하기
    if choice == 'N':
        doForest2()
    elif choice == 'S':
        doCampSite()
    elif choice == 'E':
        doWoods1()
    elif choice == 'W':
        doHouse()

# 위치: 숲2
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 플레이어가 불을 가졌다면 볼 수 있도록 하기
def doForest2():
    # 텍스트 출력하기
    print("여전히 깜깜한 숲 속입니다.")
    print("이런 곳에서는 절대 누구와도 만나고 싶지 않습니다.")
    print("이곳을 빠져나가고자 뒷걸음질합니다.")
    # 빠져나가기
    doForest1()

# 위치: 집
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 집 안에 방패가 있으므로 이를 꺼내는 코드 필요함
def doHouse():
    # 텍스트 출력하기
    print("숲속 끝에 집이 한 채 있습니다.")
    print("집이라 부르기에는 너무 낡았습니다.")
    print("집 전체가 판자로 둘러싸인 판잣집입니다.")
    print("")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "E":
        print("무엇을 하시겠습니까?:")
        print("E = 동쪽으로 간다")
        choice = input("무엇을 하시겠습니까? [E]").strip().upper()
    # 행동 수행하기
    if choice == 'E':
        doForest1()

# 위치: 산림1
def doWoods1():
    # 텍스트 출력하기
    print("삼림 속 길을 걷습니다. 이 길은 북쪽으로 이어집니다.")
    print("주위에는 온통 나무와 부러진 가지뿐 입니다. ")
    print("서쪽에는 어두운 숲이 있습니다.")
    print("뒤쪽 남쪽에는 숲 속 빈터가 있습니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "NSW":
        print("무엇을 하시겠습니까?:")
        print("N = 북쪽으로 간다")
        print("S = 남쪽으로 간다")
        print("W = 서쪽으로 간다")
        choice = input("무엇을 하시겠습니까? [N/S/W]").strip().upper()
    # 행동 수행하기
    if choice == 'N':
        doWoods2()
    elif choice == 'S':
        doClearing()
    elif choice == 'W':
        doForest1()

# 위치: 산림2
# 인벤토리 시스템을 완성했을 때를 위한 개발자 메모
# 플레이어에게 검이 있다면 이 괴물을 물리칠 수 있음
def doWoods2():
    # 텍스트 출력하기
    print("깊은 산림 속으로 향해 갑니다.")
    print("달려가다 커다란 창을 휘두르는 괴물을 만납니다.")
    print("두 개의 뿔이 난 코와 머리로 보이는 곳에 달란 화난 눈 하나 ... 그리고 역겨운 냄새!")
    print("무엇인지 확인하려는 찰나 창에 찔립니다.")
    print("무기 없이 산림을 걷는 것은 진짜 용감하거나 진짜 멍청한 것임을 깨닫기에는 너무 늦었습니다.")
    print("어떻든 이미 여러분은 쓰러진 채 움직이지 못합니다.")
    # 게임 끝내기
    doGameOver()

# 게임 끝내기
def doGameOver():
    print("Game Over!")

# 여기서 게임 시작하기
doWelcome()
doClearing()