# 1번

def my_greet():
    print('환영합니다.')
my_greet()
my_greet()


# 3번

def max2(m,n):
    if m>n:
        return m
    else:
        return n

def min2(m,n):
    if m>n:
        return n
    else:
        return m
    
print('100과 200 중 큰 수는 : ', max2(100,200))
print('100과 200 중 작은 수는 : ', min2(100,200))


# 5번

def inch2cm(inch):
    return inch*2.54
for inch in range(1,6):
    print(inch, '인치 = ', inch2cm(inch), '센티미터')


# 7번

a,b,c = map(int,input('세 수를 입력하시오 : ').split())
def mean3(a,b,c):
    return (a+b+c)/3
print(a, ',',b, ',', c, ',', '의 평균값은', mean3(a,b,c))

def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(a, ',',b, ',', c, ',', '의 최댓값은', max3(a,b,c))

def min3(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
print(a, ',',b, ',', c, ',', '의 최솟값은', min3(a,b,c))


#9번

nums = [*map(int, input('정수를 여러 개 입력하시오 : ').split())]
def mean_of_n(nums):
    return sum(nums)/len(nums)
print('평균값은 ', mean_of_n(nums))

def max_of_n(nums):
    return max(nums)
print('최댓값은 ', max_of_n(nums))

def min_of_n(nums):
    return min(nums)
print('최솟값은 ', min_of_n(nums))


# 11번
# 조건 : x1 < x2 , y1 < y2

x1 = int(input('x1 좌표를 입력하시오 : '))
y1 = int(input('y1 좌표를 입력하시오 : '))
x2 = int(input('x2 좌표를 입력하시오 : '))
y2 = int(input('y2 좌표를 입력하시오 : '))

def area(x1,y1,x2,y2):
    return ((x2-x1)*(y2-y1))/2
print('직각삼각형의 면적은 : ', area(x1,y1,x2,y2))


# 13번

# (1)
# v = 부피, s = 모서리의 길이
def v_1(s):
    return s**3
print('모서리의 길이가 12인 정육면체의 부피 : ', v_1(12))

# (2)
def v_2(s):
    return s**3
print('모서리의 길이가 20인 정육면체의 부피 : ', v_2(20))

# (3)
# w = 가로, h = 세로, l = 깊이
def v_3(w,h,l):
    return l*w*h
print('가로, 세로, 길이가 각각 3, 5, 6인 직육면체의 부피 : ', v_3(3,5,6))

# (4)
# r = 원뿔의 반지름, h = 원뿔의 높이
def v_4(r,h):
    return (1/3)*3.14*(r**2)*h
print('반지름과 높이가 각각 20, 10인 원뿔의 부피 : ', v_4(20,10))

# (5)
# r = 구의 반지름
def v_5(r):
    return (4/3)*3.14*(r**3)
print('반지름이 15인 구의 부피 : ', v_5(15))

# (6)
# r = 원기둥의 반지름
# h = 원기둥의 높이
def v_6(r,h):
    return 3.14*(r**2)*h
print('반지름과 높이가 각각 10, 20인 원기둥의 부피 : ', v_6(20,10))


# 15번
# a는 오름차순으로 정렬한 것

def my_sort(*nums):
    a = sorted(nums)
    return a

print('결과 : ', my_sort(45,6,4,56,5))


# 17번

total = 0
def sum_range(n1,n2):
    global total
    for i in range(n1,n2+1):
        total = total + i 
    return total

print('10에서 20까지의 정수의 합 : ', sum_range(10,20))


# 19번
# 피보나치 수열

n = int(input('fibo(n)의 n을 입력하세요 : '))
def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return (n-1) + (n-2)
print('fibo({}) = {}'.format(n, fibo(n)))


# 21번

n = input('주민등록번호 첫 6숫자 형식 입력 : ')
def resident_registration_number(n):
    year = int(n[:2])
    month = int(n[2:4])
    day = int(n[4:])
    
    if year>=50:
        year = year + 1900
    else:
        year = year + 2000
    
    return '{}년 {}월 {}일'.format(year,month,day)
print(resident_registration_number(n))


# 23번

import numpy as np
r = int(input('반지름을 입력하시오 : '))

while r<0:
    print('프로그램을 종료합니다.')
    break

def area_and_circumference(r):
    area = np.pi * (r**2)
    circumference = 2* np.pi * r
    return area, circumference

result = area_and_circumference(r)

print('넓이 : ', result[0], ',', '둘레 : ', result[1])


# 25번

s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

s_r1 = ''.join(s1.split()).upper()
s_r2 = ''.join(s2.split()).replace('-', '').upper()
s_r3 = ''.join(s3.split()).upper()
s_r4 = ''.join(s4.split()).replace('-','').upper()

print(s1, '(은)는', s_r1, '(으)로 수정됨')
print(s2, '(은)는', s_r2, '(으)로 수정됨') 
print(s3, '(은)는', s_r3, '(으)로 수정됨')
print(s4, '(은)는', s_r4, '(으)로 수정됨')

print(s_r1, ":", s_r1.count('N'), '개의 N이 나타남')
print(s_r2, ':', s_r2.count('N'), '개의 N이 타나남')
print(s_r3, ':', s_r3.count('N'), '개의 N이 나타남')
print(s_r4, ":", s_r4.count('N'), '개의 N이 나타남')


# 27번

frac = float(input('1보다 작고 0보다 큰 소수를 입력하세요 : '))
def unit_fraction(frac):
    closest_fraction = round(1 / frac) 
    return closest_fraction

closest_fraction = unit_fraction(frac)

print('가장 가까운 단위 분수는', 1, '/', closest_fraction, '이며,', end='')
print('이 값은 ', 1/closest_fraction, '입니다')





























