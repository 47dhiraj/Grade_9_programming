## Write a program to find the sum of digits of an entered number using a while loop.


num = int(input("Enter any number: "))

sum = 0

while num > 0:

    digit = num % 10                # only extracts last digit of that number (or only get the remainder)

    sum = sum + digit               # add digit to sum

    num = int(num / 10)
    # num = num // 10               # remove last digit (or only get the quotient)


print("Sum of digits = ", sum)