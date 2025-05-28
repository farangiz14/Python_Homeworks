#1. def is_leap(year): """ Determines whether a given year is a leap year.

def is_leap(year): 
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

for y in [2000,2001,4001,1999, 1856]:
    print(y, '-', is_leap(y))
#2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n = int(input('Enter number: '))
if n%2 == 1:
    print("Weird") 
elif n%2 == 0 and 2<= n <= 5:
    print("Not Weird")      
elif n%2 == 0 and 6<= n <= 21:
    print("Weird")
elif n%2 == 0 and n > 20:   
    print("Not Weird")
#3 Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.
# Solution 1 with if-else statement
a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
# Solution 1
if (a-b)% 2 == 0:
    print("Even numbers between a and b are: ", end = '')
    for i in range(a, b+1):
        if i%2 == 0:
            print(i, end = ' ')
# Solution 2 without if-else statement.
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

start = min(a, b)
end = max(a, b)

if start % 2 != 0:
    start += 1  

even_numbers = list(range(start, end + 1, 2))
print("Even numbers between a and b are:", even_numbers)
