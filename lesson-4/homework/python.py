# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.emp = {
    'John': 50000,
    'Jane': 60000,
    'Mike': 55000,
    'Sara': 70000
}

asc = dict(sorted(emp.items(), key=lambda item: item[1]))
print("Ascending:", asc)
dsc = dict(sorted(emp.items(), key=lambda item: item[1], reverse=True))
print("Descending:", dsc)

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
dict1 = {0:10, 1:20}
print(dict1)

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
dict1 = {0:10, 1:20}
dict2 = {2:30, 3:40}
dict3 = {4:50, 5:60}
dict4= {**dict1,
        **dict2,
        **dict3
       }   
print(dict4)

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
i = 5
dict6 = {
    i:i*i for i in range(1,i+1)
}
print(dict6)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
i = 15
dict6 = {
    i:i*i for i in range(1,i+1)
}
print(dict6)

# 1. Create a Set
# Write a Python program to create a set.
set1 = {1,2,3,4,4}
print(set1)

# 2. Iterate Over a Set
# Write a Python program to iterate over sets
set = {1,2,3,4,5}
for i in set:
    print(i)

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
set1 = {1,2,3,4,5}
set1.add(6)
print(set1)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
set1 = {1,2,3,4,5,6}
set1.remove(6)
print(set1)

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.
set1 = {1,2,3,4,5,6}
item = 4
if item in set1:
    set1.remove(item)
    
print(set1)
