1.#WAP to print all elements of a list using a for loop. 
#Take the elements of the list from the user.
# Take number of elements from user
n = int(input("Enter number of elements: "))
l = []
for i in range(n):
    elem = input("Enter element: ")
    l.append(elem)
print("Elements in the list are:")
for item in l:
    print(item)
    
2.#WAP to take inputs from user to make a list. Length of the list has to be taken from the user.
#Again take one input from user and search it in the list and delete that element, if found.
#If not found, print "Element not present".
# Take length of list
n = int(input("Enter number of elements: "))
l = []
for i in range(n):
    elem = input("Enter element: ")
    l.append(elem)
search = input("Enter element to search and delete: ")
if search in l:
    l.remove(search)
    print("Updated list:", l)
else:
    print("Element not present")

3.#WAP to print even numbers in a given range in reverse order. 
#Take the range from the user as input.
# Take range from user
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
for i in range(end, start - 1, -1):
    if i % 2 == 0:
        print(i)

4.#WAP to print odd numbers in a given range in reverse order.
#Take the range from the user as input.
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
for i in range(end, start - 1, -1):
    if i % 2 != 0:
        print(i)
#here !=0 it is an not equal to even 

