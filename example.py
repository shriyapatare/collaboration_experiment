# Function to add two numbers
def add_numbers(a, b):
    return a + b

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



# Contributor @sreekar


#area of triangle  
def area_of_triangle(p, q, r):
	# calculate the semi-perimeter  
	s = (p + q + r)/2

	# calculate the area  
	area_tri = (s*(s-p)*(s-q)*(s-r))*(0.5)  
	return area_tri


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


# Contributor @Vamshi

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

#contributor @ chaturth 
# Python program for implementation of Selection Sort
def selection_sort(A):
	# Traverse through all array elements
	for i in range(len(A)-1):
    
    		# Find the minimum element in remaining 
    		# unsorted array
    		min_idx = i
    		for j in range(i+1, len(A)):
        		if A[min_idx] > A[j]:
            		min_idx = j
            
    		# Swap the found minimum element with the first element        
    		A[i], A[min_idx] = A[min_idx], A[i]


def isPrime(n):
	is_prime = true

	for i in range(2, n):
 		if n % i == 0:
  		is_prime = false
  		break

	if is_prime:
 		print("Given integer is prime")
	else:
 		print("Given Integer isn't prime")

#driver code by contributor @shriya
int a = input("Enter the number corresponding to the operation to execute that operation:\n1. Add 2 numbers.\n2.Find the nth number in the Fibonacci series.\n3. Merge Sort an array.\n4. Bubble sort an array.\n5. Find the area of a triangle. \n6. Find LCM of 2 numbers.\n7. Check if a string if a palindrome.\n8. Selection sort an array.\n9. Find if a number is prime or not. ")
if(a==1):
	x = input("Enter first number")
	y = input("Enter second number")
	print("Sum of ", x, " and ", y, " is: ", add_numbers(x, y))

elif(a==2):
	x = input("Enter the number")
	ans = funbonci(x)
	print(f"The {x}th Fibonacci number is: {ans}")

elif(a==3):
	arr = list(map(int, input("Enter the array elements separated by space: ").split()))
	merge_sort(arr)
	print("Sorted array is: ", arr)

elif(a==4):
	arr = list(map(int, input("Enter the array elements separated by space: ").split()))
        bubble_sort(arr)
        print("Sorted array is: ", arr)

elif(a==5):
	p = input("Enter first side:")
	q = input("Enter second side:")
	r = input("Enter third side:")
	area = area_of_triangle(p, q, r)
	print(f"Area of triangle is: {area}")

elif(a==6):
	x = input("Enter first number")
	y = input("Enter second number")
	lcm = calc_lcm(x, y)
	print("The LCM of the provided two numbers is", lcm)

elif(a==7):
	word = input("Enter a word to check if it's a palindrome: ")
	print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

elif(a==8):
	arr = list(map(int, input("Enter the array elements separated by space: ").split()))
        selection_sort(arr)
        print("Sorted array is: ", arr)
	
elif(a==9):
	x  = input("Enter an integer greater than 2")
	isPrime(x)



