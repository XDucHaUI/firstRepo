from decimal import*
from math import*



print("Chin chào tất cả các bạn mình là Ngô Lê Xuân Đức") # đây là một câu lệnh dài vcl
# sau đây mình sẽ cùng các bạn làm một bài toán nhé
#HÃy tính tổng các số nguyên dương từ 1 đến 10

a = -11
b = 55
print(fabs(a))
c=a+b
d=a-b
e=a*b
f=a/b
print(" c = a + b",c)
#print(type(c))
print(" d = a - b",d)
#print(type(d))
print(" e = a x b",e)
#print(type(e))
getcontext().prec = 5
f = Decimal(5000)/Decimal(465)
print(" f = a : b",f)
#print(type(f))

