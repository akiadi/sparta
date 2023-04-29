# 라이브러리 불러오기
import datetime

# 오늘 날짜 가져오기
today = datetime.datetime.now()

# 요일에 따라 다른 메시지 출력하기
# if today.weekday() == 5 or today.weekday() == 6:
if today.weekday() in [5, 6]:
    # 토요일과 일요일에 출력할 내용
    print("주말이므로 학교에 가지 않습니다!")
    print("온종일 코딩하며 지낼 수 있어요!")
elif today.weekday() == 4:
    # 금요일에 출력할 내용
    print("금요일이므로 내일이면 코딩하며 시간을 보낼 수 있어요!")
else:
    # 그 외 요일에 출력할 내용
    print("오늘은 학교 가는 날입니다.")
