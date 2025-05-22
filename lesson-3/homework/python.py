# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
fruts_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
fruts_list [2]

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
l1 = [1,2,3]
l2 = [1,4,5]
concat_list = l1+l2
print(concat_list)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
list = [50, 60, 70, 80,90]
first = list[0]
middle = list[len(list)//2]
last = list[-1]

new_list = [first, middle, last]
print(new_list)

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
list = [ 'Anna', 'Bob', 'Charlie', 'David', 'Eva']
tup = tuple(list)
type(tup)

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['London', 'New York', 'Tokyo', 'Paris', 'Berlin']

if 'Paris'  in cities:
    print('Paris is in the list')
else:
    print('Paris is not in the list')
  
# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3, 4, 5]
duplicated_List = numbers * 2
print(duplicated_List)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
numbers = [1, 2, 3, 4, 5]

numbers[0], numbers[-1] = numbers[-1], numbers[0]
numbers

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
tuples = (1,2,3,4,5,6,7,8,9,10)
sliced_tuples = tuples[3:7]
print(sliced_tuples)

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
colors = ('red','blue','green','blue','yellow','blue','red')
count_blues = colors.count('blue')
print(count_blues)

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".
animals = ('cat', 'dog', 'lion', 'tiger')
index_lion = animals.index('lion')
print(index_lion)

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
tuples = (1,2,3,4,5,6,7,8,9,10)
animals = ('cat', 'dog', 'lion', 'tiger')
tuples + animals

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

length_tuple = len(animals)
print(length_tuple)

length_colors = len(colors)
print(length_colors)

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
tups = (1,2,3,4,5)
tups_list = list(tups)
print(tups_list)

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (10, 20, 5, 30, 15)
max_v =max(numbers)
min_v = min(numbers)
print(max_v)
print(min_v)

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
tups = (1,2,3,4,5)
reversed_taps = tups[::-1]
print(reversed_taps)
