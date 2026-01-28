user_name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
location = input("Enter your location: ")

if age.isdigit() and int(age) >= 20 and user_name.isupper() and "@" in email and "." in email:
    print(f"Welcome {user_name} from {location}! You are eligible to register with the email {email}.")
else:
    print(f"sorry {user_name}, you must be at least 20 years old to register.")

if email.count("@") != 1:
    print("Invalid email: must contain exactly one '@' symbol.")
elif email.startswith("@") or email.endswith("@"):
    print("Invalid email: '@' cannot be at the start or end.")