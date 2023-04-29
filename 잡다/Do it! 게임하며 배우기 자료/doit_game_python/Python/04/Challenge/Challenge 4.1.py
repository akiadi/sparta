# 라이브러리 불러오기
import datetime

# 오늘 날짜 구하기
today = datetime.datetime.now()

# 오늘의 연도, 월, 일, 시, 분 출력하기
print("지금은", today.year, "년입니다.")
print("지금은", today.month, "월입니다.")
print("지금은", today.day, "일입니다.")
print("지금은", today.hour, "시입니다.")
print("지금은", today.minute, "분입니다.")