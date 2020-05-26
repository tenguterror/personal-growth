# This is a combination of the code I came up with and the code from StackOverflow

myList = []



while True:
    print('Enter a new value, or exit to stop.')
    response = input()
    if response == 'exit':
        break
    myList.append(response)

def commaCode(eggs):
    return ', '.join(map(str,eggs[:-1])) + ' and ' + str(eggs[-1])

print(commaCode(myList))



#myList.insert(-1, 'and')

#print(', '.join(myList))