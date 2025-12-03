'''
Create a list of 5 friends' names. Ask a user to input the name of any friend. 

If the user entered name is in that friend"s list then display that entered name, otherwise display sorry entered name not found.
'''


## Easy: Example 1:

friends = ["John", "Jack", "Aash", "Michael", "Xavi"]

name = input("Enter your friend's name: ")

if name in friends:
    print("Friend found: ",name)
else:
    print("Sorry, ", name, "not found.")



## Advance: Example 2

friends = ["Sita", "Gita", "Aash", "Michael", "Xavi"]

for i in range(len(friends)):                           # make all names lowercase in the same list
    friends[i] = friends[i].lower()

name = input("Enter your friend's name: ")


if name.lower() in friends:
    print("Friend found: ", name)
else:
    print("Sorry,", name, "not found.")

