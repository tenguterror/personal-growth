#! python3
# This is to print fizzBuzz.
# if number divisiable by 3 and 5 print fizz buzz.
# if number divisable by 3 print fizz.
# if number is divisable by 5 print buzz.

nums = input('Enter a number:')  # Asks for a number.
nums = int(nums)  # Converts a string into a interger.


def fizzBuzz(nums):  # This is our main function
    # This loop will go through all the numbers from 1 up to the number the user inputs.
    for i in range(1, nums + 1):
        # Checks to see if the number is divisable between 3 and 5. Both have to to be true.
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:  # Checks to see if only divisable by 3.
            print('Fizz')
        elif i % 5 == 0:  # Checks to see if divisable by 5.
            print('Buzz')
        else:            # If no conditions are met above it will print out the number
            print(i)


# This will call the function fizzBuzz and add the input nums to it.
fizzBuzz(nums)
