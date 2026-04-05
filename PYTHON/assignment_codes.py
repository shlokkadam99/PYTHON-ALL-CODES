#Q)Python program to determine whether a number is Prime
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



#Q)Program to calculate the factorial of a number using a loop
num = int(input("Enter a number: "))
factorial = 1

# Check if the number is negative, positive or zero
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}.")



#Q)Program to generate Fibonacci sequence until n terms
n_terms = int(input("How many terms? "))

# First two terms
n1, n2 = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print(f"Fibonacci sequence upto {n_terms}:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1, end=" ")
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1
print() # For new line


#Q6: Program to determine if a number is a palindrome
num = int(input("Enter a number: "))
temp = num
reverse_num = 0

while temp > 0:
    digit = temp % 10
    reverse_num = (reverse_num * 10) + digit
    temp = temp // 10

if num == reverse_num:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")


#Q7: Program to calculate the total value of digits in a number
num = input("Enter a number: ")
total_sum = 0

for digit in num:
    total_sum += int(digit)

print(f"The sum of digits of {num} is: {total_sum}")



#Q8: Program to organize a list into ascending order
my_list = [64, 34, 25, 12, 22, 11, 90]

# Using the sort() method
my_list.sort()

print("Sorted list (Ascending):", my_list)



#Q9: Program to determine maximum and minimum values in a list
my_list = [10, 50, 5, 100, 35, 2]

# Using built-in functions
max_val = max(my_list)
min_val = min(my_list)

print(f"List: {my_list}")
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")


#Q10: Program to eliminate all repeated items from a list
raw_list = [1, 2, 2, 3, 4, 4, 5]

# Using set to remove duplicates, then converting back to list
unique_list = list(set(raw_list))

print("Original List:", raw_list)
print("List without duplicates:", unique_list)



#Q11: Program to arrange data in both ascending and descending order
data = [15, 2, 45, 10, 8]

# Ascending
data.sort()
print("Ascending Order:", data)

# Descending
data.sort(reverse=True)
print("Descending Order:", data)



#Q12: Program to determine how many times an element appears in a tuple
my_tuple = (10, 20, 30, 20, 40, 20, 50)
element = 20

count = my_tuple.count(element)

print(f"The element {element} appears {count} times in the tuple.")



#Q13: Tuple Packing and Unpacking Demonstration
# Tuple Packing
packed_tuple = ("Computer Science", "B.Tech", 2)
print(f"Packed Tuple: {packed_tuple}")

# Tuple Unpacking
branch, degree, year = packed_tuple

print("--- Unpacked Data ---")
print(f"Branch: {branch}")
print(f"Degree: {degree}")
print(f"Year: {year}")



#Q14: Program to transform a tuple into a list
my_tuple = ("Apple", "Banana", "Cherry")

# Converting to list
my_list = list(my_tuple)

print(f"Original Tuple: {my_tuple} (Type: {type(my_tuple)})")
print(f"Converted List: {my_list} (Type: {type(my_list)})")


#Q17: Program for Set Union, Intersection, and Difference
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Union
print("Union:", set_A | set_B)

# Intersection
print("Intersection:", set_A & set_B)

# Difference (A - B)
print("Difference (In A but not B):", set_A - set_B)


#Q18: Program to use a Set to eliminate duplicates from a List
# This is a practical example of cleaning data
raw_data = ["red", "blue", "red", "green", "blue", "blue"]

# Convert to set to remove duplicates
unique_set = set(raw_data)

# Convert back to list if needed
clean_list = list(unique_set)

print(f"Original with duplicates: {raw_data}")
print(f"Cleaned data: {clean_list}")



#Q20: Program demonstrating Arithmetic and Comparison operators
a = 10
b = 3

print("--- Arithmetic Operators ---")
print(f"Addition ({a} + {b}): {a + b}")
print(f"Floor Division ({a} // {b}): {a // b}")  # Removes decimal part
print(f"Modulus ({a} % {b}): {a % b}")        # Remainder
print(f"Power ({a} ** {b}): {a ** b}")

print("\n--- Comparison Operators ---")
print(f"Is {a} greater than {b}? {a > b}")
print(f"Is {a} equal to {b}? {a == b}")
print(f"Is {a} not equal to {b}? {a != b}")


#Q21: Program to create a dictionary, display keys/values, and show methods
# Creating a dictionary
student = {
    "name": "Amit",
    "roll_no": 101,
    "city": "Pune"
}

print("Original Dictionary:", student)

# Displaying all Keys
print("Keys:", list(student.keys()))

# Displaying all Values
print("Values:", list(student.values()))

# Method: get() (Safe way to access data)
print("Get Name:", student.get("name"))

# Method: update() (Adding/Updating data)
student.update({"course": "CSE"})
print("After Update:", student)

# Method: pop() (Removing an item)
student.pop("city")
print("After Pop:", student)



#Q22: Program to count character frequency in a string using a dictionary
text = "engineering"
freq_dict = {}

for char in text:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

print(f"String: {text}")
print("Character Frequency:", freq_dict)