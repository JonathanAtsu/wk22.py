# write a script that takes string from user and it will tell how vowels are in the string


user_input = input("Enter a string: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
result = []
for char in user_input:
    if char in vowels:
     result.append(char)
nuber = len(result)
print(f"The number of vowels in the string is: {nuber}")