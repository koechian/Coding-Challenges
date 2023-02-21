# given a number n, for integer i in the range from 1 to n, print:
# FizzBuzz - if the number is a multiple of both 3 and 5
# Buzz - if the number is a multiple of 5 but not 3
# Fizz - if the number is a multiple of 3 but not 5
# i - if the number is not a multiple of either


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        else:
            print(i)


fizzbuzz(15)
