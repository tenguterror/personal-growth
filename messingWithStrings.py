# This will ask for the user name and print it out last then first.
# This was done using string formatting(f strings) and string methods so is the user inputs in lower it will titlecase it

print('Hello, what is you first name?')
firstName = input().title()
print('What is you last name?')
lastName = input().title()

print(f'Hello {lastName}, {firstName}.')