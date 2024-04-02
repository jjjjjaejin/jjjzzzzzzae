# 1번

list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3

# (1)
print(list_ex[low])

# (2)
print(list_ex[low+2])

# (3)
print(list_ex[high-low])

# (4)
print(list_ex[low-high])

# (5)
print(list_ex[-1]) 

# (6)
print(list_ex[-low])

# (7)
print(list_ex[2*3])

# (8)
print(list_ex[2]*3)

# (9)
print(list_ex[5%4])

# (10)
print(len(list_ex))



# 3번

list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for n in list1:
    for m in list2:
        result = n*m
        print('{} * {} = {}'.format(n,m,result))



# 5번

list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

for n in list1:
    for m in list2:
        result = n + ' ' + m
        print(result)



# 7번

n_list = [10, 20, 30, 50, 60]
n_list_sum = 0

for i in n_list:
    n_list_sum += i
    
print('리스트 원소들 : ', n_list)
print("리스트 원소들의 합 : ", n_list_sum)



# 9번

n_list = [10, 20, 30, 50, 60]
n_list_max = n_list[-1]

for i in n_list:
    if i > n_list_max:
        n_list_max = i
        
print('리스트의 원소들 : ', n_list)
print('리스트의 원소들 중 최댓값 : ', n_list_max)



# 11번

a,b,c,d,e = map(int,input('5개의 수를 입력하세요 : ').split())
n_list = [a,b,c,d,e]

print('합 : ', sum(n_list))
print('평균 : ', sum(n_list)/len(n_list))
print('최댓값 : ', max(n_list))
print('최솟값 : ', min(n_list))



# 13번

n = [*map(int,input('10개의 수를 입력하세요 :').split())]
mean = sum(n)/len(n)

print('합 : ', sum(n))
print('평균 : ', mean)

def standard_deviation(n):
        sigma = (sum((x-mean)**2 for x in n)/len(n))**(1/2)
        return sigma
    
print('표준편차 : ', round(standard_deviation(n),2))



# 15번

greet = 'Have a beautiful day.'

print(greet[0:4])
print(greet[7:16])
print(greet[17:20])



# 17번

animals = ['dog', 'cat', 'tiger', 'lion']
print('animals = ', animals)



# 19번

s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

print('s_list = ', s_list)

for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)
print('new_s_list = ', new_s_list)



# 21번

src = 'a2b3c6a2c3f1g1'

for ch in src:
    if ch.isnumeric():
        for i in range(int(ch)):
            print(ch_old, end='')
    else:
        ch_old=ch



# 23번

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

person_list = person1 + person3 + person4

def how_many_persons(person_list):
    return len(person_list)//5

n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')
