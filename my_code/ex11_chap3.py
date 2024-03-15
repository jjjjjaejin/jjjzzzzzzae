# 2024/03/15
# 복권번호 추첨


a,b,c=map(int,input('세 복권번호를 입력하시오:').split())



my_numbers = [a, b, c]
numbers = [2, 3, 9]

match_numbers = len(set(my_numbers) & set(numbers))

if match_numbers==3:
    print('상금 1억 원')
elif match_numbers==2:
    print('상금 1천만 원')
elif match_numbers==1:
    print('상금 1만 원')
else:
    print('다음 기회에...')
