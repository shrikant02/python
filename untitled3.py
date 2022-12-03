student = { 'name':'John', 'age':12, 'courses':['Art', 'Math', 'CompSci']}

#student['phone'] = '555-555-555'

student.update({'name':'Bill', 'age': 15, 'phone':'555-999-222'})

print(student['age'])


print(student.get('phone', ":("))

del student['age']  # pop also can be used

print(student)

print(len(student))

print(student.items())

for key, value in student.items():
    print(key, value)

