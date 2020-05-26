# Grabbed this code from StackOverflow as an example of another way to do this 
def commaCode(eggs):
    return ', '.join(map(str,eggs[:-1])) + ' and ' + str(eggs[-1])
spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))