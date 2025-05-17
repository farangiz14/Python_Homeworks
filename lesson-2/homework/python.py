#1. Age Calculator
name = input("Enter your name: ")
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
today = date.today().year
age = today - int(birthdate.split('-')[0])
print(f"Hello, {name}, you are {age} years old.")

#2. Extract Car Names
text = 'LMaasleitbtui'.lower()

if 'm' in text and 'a' in text and 'l' in text and 'i' in text and 'b' in text and 'u' in text:
    print('Found: Malibu')
else: 
    print('Not found')

#3. Extract Car Names
txt = 'MsaatmiazD'.lower()

if 'm' and 'a' and 't' and 'i' and 'z' in txt:
    print('Found: Matiz')
else:
    print('Not found')

#4. Extract Residence Area
txt = "I'am John. I am from London"
location = txt.split(' ')[-1]
print(f"Location: {location}")

#5. Reverse String
user_input = input("Enter a text: ")
reverse =  user_input[ ::-1]
print(f'Reversed text: {reverse}')

#6. Count Vowels
txt = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
 
for char in txt:
    if char in vowels:
        count += 1
  
print(f"Number of vowels: {count}")

#7. Find Maximum Value
nums = list(map(int, input("Enter numbers: ").split()))
print("Max value:", max(nums))

8. Check Palindrome
word = input('enter owrds: ').lower()
if word == word[ : :-1]:
    print('Palidrome')
else:
    print('Not Palindrome')

#9. Extract Email Domain
email = input("Enter your email: ")
domain = email.split('@')[1]
print(f'DomainL {domain}')

#10. Generate Random Password
import random, string
len = int(input('Enter password length: '))

generate_pass = string.ascii_letters + string.digits + string.punctuation
password = (''.join(random.sample(generate_pass, int(len))))
print(f'password: {password}')
