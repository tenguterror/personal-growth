myList = []

while True:
    print('Enter a new value, or exit to stop.')
    response = input()
    if response == 'exit':
        break
    myList.append(response)
myList.insert(-1, 'and')
print(', '.join(myList))