#2.1
year=(int(input("Enter year:")))
if(year%400==0 or (year%4==0 and year%100!=0)):
  print(year,"is a leap year")
else:
  print(year,"is not a leap year")


#2.2
marks = []
n=int(input("Enter number of subjects:"))
for i in range(n):
    m=int(input(f"Enter marks of subject {i+1}:"))
    marks.append(m)
avg=sum(marks)/n
if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 50:
    grade = "D"
else:
    grade = "Fail"
print("Average:", avg)
print("Grade:", grade)


#2.3
a= []
for i in range(3):
    m=int(input(f"Enter Three Numbers, number {i+1}:"))
    a.append(m)
if(a[0]==a[1]==a[2]):
    print("All numbers are equal")
elif(a[0]>a[1]>a[2]):
  print("First number is greatest:",a[0])
elif(a[0]<a[1]<a[2]):
  print("Third number is greatest:",a[2])
elif(a[1]>a[0]>a[2]):
  print("Second number is greatest:",a[1])