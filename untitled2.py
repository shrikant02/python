list_1 = ['History', "Math", 'Physics', 'CompSci']

list_2 = list_1

list_1[0] = 'Art'

print(list_1)
print(list_2) # they both same mutable object


# Tuple #Immutable

list_1 = ('History', "Math", 'Physics', 'CompSci')

list_2 = list_1

#list_1[0] = 'Art' # error

print(list_1)
print(list_2)

#Sets 
courses = {'History', "Math", 'Physics', 'CompSci', 'Math'} # remove duplicates

print(courses)




