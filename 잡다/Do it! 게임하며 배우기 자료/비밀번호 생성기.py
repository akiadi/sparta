import string
import random

user_Input = input('비밀번호에 추가하고 싶은 것을 고르세요(문자, 숫자, 기호): ')
Randnumder = ""

for Password_puls in user_Input:
    if Password_puls == '문':
        Randnumder += string.ascii_uppercase
    elif Password_puls == '기':
        Randnumder += string.punctuation
    elif Password_puls == '숫':
        Randnumder += string.digits


while True:
    Randnumder_str = ''.join(Randnumder)
    randNumder = ''
    for i in range(8):
        randNumder += random.choice(Randnumder_str)     
    print(randNumder)
    uinput = input('새로운 비밀번호를 원하신다면 엔터, 만족하셨다면 OK를 작성해주세요.').strip().upper()
    if uinput == 'OK':
        break