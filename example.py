# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

# Contributor @parikshith078
def funbonci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b

# Contributor @shashank-g2100
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return sorted_merge(left, right)

def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + sorted_merge(left[1:], right)
    else:
        return [right[0]] + sorted_merge(left, right[1:])





# Contributor @jeevan
def bubble_sort(arr):

    for n in range(len(arr) - 1, 0, -1):

        for i in range(n):
            if arr[i] > arr[i + 1]:

                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)



# Contributor @sreekar


#area of triangle  

p = float(input('Enter the length of first side: '))  
q = float(input('Enter the length of second side: '))  
r = float(input('Enter the length of final side: '))  

# calculate the semi-perimeter  
s = (p + q + r)/2

# calculate the area  
area_tri = (s*(s-p)*(s-q)*(s-r))*(0.5)  
print('The area of the triangle is %0.2f' %area_tri)



# Contributor @Lohith


# Function to calculate LCM
def calc_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function and print the result
print("The LCM of the provided two numbers is", calc_lcm(num1, num2))



# Contributor @Vamshi

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

# Getting user input
word = input("Enter a word to check if it's a palindrome: ")
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")


#contributor @ chaturth 
# Python program for implementation of Selection
# Sort
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)-1):
    
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print(A[i],end=" ") 




user_int = input("Enter an integer greater than 2")
is_prime = true

for i in range(2, user_int):
 if user_int % i == 0:
  is_prime = false
  break

if is_prime:
 print("Given integer is prime")
else:
 print("Given Integer isn't prime")

