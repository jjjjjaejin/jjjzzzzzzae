# 1번

# (1)
n = 123
n.__add__(334)

# (2)
n.__sub__(334)

# (3)
n.__mul__(334)

# (4)
n.__truediv__(3)




# 3번

s = 'Hello World~'

p = s.pop() # 불가능
z = s.sort() # 불가능
a = s.append() # 불가능
u = s.upper() # 가능
i = s.insert() # 불가능
r = s.remove() # 불가능




# 5번

a = 1
b = 1
c = 2
d = 3
e = 3

print('a와 b는 같은 객체인가?', a is b)
print('b와 c는 같은 객체인가', b is c)
print('c와 d는 같은 객체인가?', c is d)
print('d와 e는 같은 객체인가?', d is e)




# 7번

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '이름은 '+self.name+'이고, 나이는 '+self.age+'살 입니다.'

my_dog = Dog('Mangoo', '3')

print(my_dog)





# 9번

class Counter:
    def __init__(self, number):
        self.number = number

    def inc(self):
        self.number += 1
        if self.number >= 100:
            self.reset()
                
    def dec(self):
        self.number -= 1
        if self.number <= -1:
            self.reset()
            
    def reset(self):
        self.number = 0
        
    def __add__(self,other):
        return Counter(self.number + other.number)
    
    def __sub__(self,other):
        return Counter(self.number - other.number)

                
c1 = Counter(10)
c2 = Counter(20)

c3 = c1 + c2
c4 = c1 - c2

print('c3 = ', c3.number)
print('c4 =', c4.number)





# 11번

class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.korean_quiz = None
        self.math_quiz = None
        self.science_quiz = None
        
    def set_korean_quiz(self, score):
        self.korean_quiz = score
        
    def set_math_quiz(self, score):
        self.math_quiz = score
        
    def set_science_quiz(self,score):
        self.science_quiz = score
        
    def get_total_score(self):
        total_score = self.korean_quiz + self.math_quiz + self.science_quiz
        return total_score
    
    def get_avg_score(self):
        total_score = self.get_total_score()
        avg_score = total_score / 3
        return avg_score
    
        
name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')

student = Student(name, student_id)     
        
korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))


student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)

print('이름 : ', student.name, '학번 : ', student.student_id)
print('국어성적 : ', student.korean_quiz, '수학성적 : ', student.math_quiz, '과학성적 : ', student.science_quiz)
print('합계 : ', student.get_total_score(), '평균 : ', student.get_avg_score())







# 13번

class Rectangle:
    def __init__(self,x,y,width,height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
    
    def __str__(self):
        return "(x = {}, y = {}, w = {}, h = {})".format(self.__x, self.__y, self.__width, self.__width)
    
    def area(self):
        return self.__width*self.__height
        
    def overlaps(self,other):
        return (self.__x < other.__x + other.__width and self.__x + self.__width > other.__x and self.__y < other.__y + other.__height and self.__y + self.__height > other.__y)
    
    def contains(self,other):
        return (self.__x <= other.__x and self.__y <= other.__y and self.__x + self.__width >= other.__x + other.__width and self.__y + self.__height >= other.__y + other.__height)
        
    
r1 = Rectangle(0,0,100,100)
r2 = Rectangle(0,-10,10,10)
r3 = Rectangle(-100,0,120,100)

print('r1 = Rectangle :', r1, ', 면적 :', r1.area())
print('r2 = Rectangle :', r2, ', 면적 :', r2.area())
print('r3 = Rectangel :', r3, ', 면적 :', r3.area())

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))




# 추가 6번

class Car:
    def method(self):
        print('슈퍼 클래스')
        
class Sedan(Car):
    def method(self):
        print('서브 클래스')
        
myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()
# 정답은 3번 (슈퍼 클래스, 서브클래스)






# 추가 7번

class Car:
    speed = 0
    
    def upSpeed(self,value):
        self.speed = self.speed + value
        
class RVCar(Car):
    seatNum = 0
    
    def getSeatNum(self):
        return self.seatNum
    
myCar = RVCar()
myCar.upSpeed(1000)
print(myCar.speed)
# 정답은 class RVCar(Car)


