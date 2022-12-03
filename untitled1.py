courses = ['History', "Math", 'Physics', 'CompSci']
courses_2 = ["Art", "Education"]

print(len(courses))


print(courses[0:2]) # start from index 0 till 2 not including 2

print(courses[:2]) # assuemed we wanted to start from zero
print(courses[2:])

#courses.insert(0, courses_2) # list inside list
#courses.extend(courses_2)
    

#popped = courses.pop()

#courses.sort(reverse=True)

sorted_courses = sorted(courses) # we did not loose the original list

'''for index, item in enumerate(courses, start=1):
    print(index, item)'''

course_str = ", ".join(courses)

new_list = course_str.split(", ")

print(course_str)
print(new_list)

#print(courses)




