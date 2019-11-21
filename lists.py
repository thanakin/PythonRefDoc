'''
List Methods

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''

thislist = ["apple", "banana", "cherry"]
print(thislist)


thislist2 = ["apple", "banana", "cherry"]
print(thislist2[1])


thislist3 = ["apple", "banana", "cherry"]
print(thislist3[-1])


thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[2:5])


thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[-4:-1])


thislist6 = ["apple", "banana", "cherry"]
thislist6[1] = "blackcurrant"
print(thislist6)


thislist7 = ["apple", "banana", "cherry"]
for x in thislist7:
    print(x)


thislist8 = ["apple", "banana", "cherry"]
if "apple" in thislist8:
    print("Yes, 'apple' is in the fruits list")


thislist9 = ["apple", "banana", "cherry"]
print(len(thislist9))


thislist10 = ["apple", "banana", "cherry"]
thislist10.append("orange")
print(thislist10)


thislist11 = ["apple", "banana", "cherry"]
thislist11.insert(1, "orange")
print(thislist11)


thislist12 = ["apple", "banana", "cherry"]
thislist12.remove("banana")
print(thislist12)


thislist13 = ["apple", "banana", "cherry"]
thislist13.pop()
print(thislist13)


thislist14 = ["apple", "banana", "cherry"]
del thislist14[0]
print(thislist14)


thislist15 = ["apple", "banana", "cherry"]
del thislist15
#print(thislist15)


thislist16 = ["apple", "banana", "cherry"]
thislist16.clear()
print(thislist16)


thislist17 = ["apple", "banana", "cherry"]
mylist = thislist17.copy()
print(mylist)


thislist18 = ["apple", "banana", "cherry"]
mylist = list(thislist18)
print(mylist)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print('list2:', list1)


ist1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print('list1:', list1)


thislist19 = list(("apple", "banana", "cherry")) # note the double round-brackets
print("list19:", thislist19)