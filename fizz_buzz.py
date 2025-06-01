# Loop through numbers from 1 to 100
for num in range(1, 101):

    # If the number is divisible by both 3 and 5 (no remainder), print "FizzBuzz"
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')

    # If the number is divisible by 3 only, print "Fizz"
    elif num % 3 == 0:
        print('Fizz')

    # If the number is divisible by 5 only, print "Buzz"
    elif num % 5 == 0:
        print('Buzz')

    # If the number is not divisible by 3 or 5, just print the number
    else:
        print(num)
