year=int(input('판별할 연도를 입력하세요:'))

결과 = year%4==0 and year%100!=0 or year%400==0

print(f"{year}년은 {결과}")
