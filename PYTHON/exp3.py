#3.1
a=int(input("Enter a number to reverse: "))
rn=0
while a!=0:
    d=a%10
    rn=rn*10+d
    a=a//10
print(rn)


#3.2
num=2
while num<=100:
    print(num)
    num+=2


#3.3
# star pattern middle one
n = 3
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))



#3.4
#star pattern start
for i in range(1, 4):
    print('*' * i)
