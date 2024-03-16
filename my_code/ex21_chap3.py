# 2024/03/16
# 소수 판별

n = int(input('숫자를 입력하세요:'))

prime_number = True

for i in range (2, n):
    if n % i == 0:
        prime_number = False
        break

if prime_number:
    print(n, '은 소수입니다.')

else:
    print(n, '은 소수가 아닙니다')



