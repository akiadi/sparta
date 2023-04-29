import datetime

mm = int(input('태어난 월을 입력하세요: '))
dd = int(input('태어난 일을 입력하세요: '))

today = datetime.date.today()
birthday = datetime.date(today.year, mm, dd)

if birthday < today:
    birthday = datetime.date(today.year +1, mm, dd)

total_calculation = (birthday - today).days
print(total_calculation)

