import random

while True:
    hum=input('가위 바위 보 선택(종료는 엔터키):')
    if hum == '':
        break
    if hum not in ['가위','바위','보']:
        print('다시 입력하세요!')
        print('')
        continue

    com = random.choice(['가위','바위','보'])
    print('컴퓨터: ', com)
    if hum == com:
        print('무승부')
    elif hum == '가위' and com == '바위':
        print('컴퓨터 승리!')
    elif hum == '바위' and com == '보':
        print('컴퓨터 승리!')
    elif hum == '보' and com == '가위':
        print('컴퓨터 승리!')
    elif com == '가위' and hum == '바위':
        print('사람 승리!')
    elif com == '바위' and hum == '보':
        print('사람 승리!')
    elif com == '보' and hum == '가위':
        print('사람 승리!')
    print('-'*40)
    print('')




