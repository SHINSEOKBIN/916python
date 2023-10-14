import time
import random

mychars=''
li = ['thunderbolt','mustang','wildcat','corsair','hellcat','lightning','dauntless','helldiver']
answer = random.choice(li)
chance = len(answer)+5

print('게임이 시작됩니다')
time.sleep(1)
print('_'*len(answer))

while True:
    success=1
    chance -= 1
    if chance==0:
        print("실패! 남은 기회가 없어요...")
        print("정답은",answer,"였습니다...")
        break

    char=input('추측 문자 입력: ')
    if len(char) != 1:
        print("알파벳 하나만 입력하세요!")
        print()
        continue
    chance -= 1
    mychars += char.lower()

    if char not in answer:
        print("틀렸습니다")

    for w in answer:
        if w in mychars:
            print(w,end=' ')
        else:
            print('_',end='')
            success=0

    if success == 1:
        print()
        print("정답! 축하합니다!")
        break
    print()





