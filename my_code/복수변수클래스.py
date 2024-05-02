# 복수 변수 클래스
# 더하기, 빼기, 곱하기, 나누기

class comx:
    def __init__(self,x,y):
        self.real=x
        self.imag=y
     
    # 더하기
    def __add__(self,other):
        return comx(self.real + other.real, self.imag + other.imag)
    
    # 빼기
    def __sub__(self,other):
        return comx(self.real - other.real, self.imag - other.imag)
    
    # 곱하기
    def __mul__(self,other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.real + self.imag * other.imag 
        return comx(real_part, imag_part)
    
    # 나누기
    def __truediv__(self,other):
        d = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / d
        imag_part = (self.imag * other.real - self.real * other.imag) / d
        return comx(real_part, imag_part)
    
a = comx(1,2)
b = comx(2,3)

c = a + b
d = a - b
e = a * b
f = a / b

print(c.real, '+', c.imag, 'i')   
print(d.real, '+', d.imag, 'i')
print(e.real, '+', e.imag, 'i')
print(f.real, '+', f.imag, 'i')
