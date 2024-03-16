# 2024/03/16
# 1부터 n까지 제곱의 합

n = int(input('숫자를 입력하세요:'))
s = 0

for i in range(1,n+1):
    s += i**2

print('결과는 ', s, '입니다.')
