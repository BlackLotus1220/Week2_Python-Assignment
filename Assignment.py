#Inserting at specific index
my_list=[10, 20, 30, 40]
#insert '15' at index 1
my_list.insert(1, '15')
print(my_list)


#Extending [50,60,70]
list_1=[10, 20, 30, 40]
list_2=[50, 60, 70]
list_1.extend(list_2)
print(list_1)


#Removing the last statement
del my_list[-1]
print(my_list)
del list_2[-1]
print(list_2)

#Sorting in ascending order
list_1=[20, 40, 10, 30, 70, 50, 60]
list_1.sort()
print(list_1)

#Sorting in descending order
list_1=[20, 40, 10, 30, 70, 50, 60]
list_1.sort(reverse=True)
print(list_1)

#Iterating through a list
list_1=[20, 40, 10, 30, 70, 50, 60]
index=[list_1.index(30)]
print(index)

