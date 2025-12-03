## Write a program in python to find the first 10 even numbers using a for loop.


## Best & easy way:

for i in range(2, 21, 2):
    print(i)



## Another best & easy way:

num = 2

while num <= 20:

    if num % 2 == 0:
        print(num)


    num += 1



## Another way (rarely used):

for i in range(1, 11):      
    print(i * 2)            

