#1.1
name=(input("Enter your name : "))
surname=(input("Enter your surname : "))
print(name)
print(surname)


#1.2
a = 10
b = 15

print("Arithmetic Operators")
print("Addition : ", a + b)
print("Subtraction : ", a - b)
print("Multiplication : ", a * b)
print("Division : ", a / b)
print("Modulus : ", a % b)

print("Logical Operators")
print("a>b and a==10", a > b and a == 10)
print("a<b or b==75", a < b or b == 75)
print("not (a==b)", not (a == b))

print("Bitwise operators")
print("Bitwise AND (a & b)", a & b)
print("Bitwise OR (a | b)", a | b)

print("\n Identify operators")
m = a
n = 10
print("m is a", m is a)
print("a is n", a is n)
print("a is not b", a is not b)


#1.3
side=(int(input("Enter the side of square : ")))
area=side*side
perimeter=4*side
print("Area of square : ",area)
print("Perimeter of square : ",perimeter)


#1.4
a=(int(input("Enter the first number : ")))
b=(int(input("Enter the second number : ")))
temp=a
a=b
b=temp
print("After swapping a : ",a)
print("After swapping b : ",b)