# 2024/03/15
# 2개의 정수를 입력 받아 작은 수부터 나열

a,b = map(int,input("두 젇수를 입력하시오:").split())

if a<b:
    print(a,b)
else:
    print(b,a)
