# =============================================================================
# def hello_func():
#     pass   # it will not throw error for leaving it empty we will work with it later   
# =============================================================================

def hello_func(greeting, name = "You"):
    return '{}, {}'.format(greeting, name)
    
#print(hello_func('Hi', name = 'Shrikant'))

def student_info(*args, **kwarg): # (positional args, keyword args)
    print(args)
    print(kwarg)
    
#student_info('Science', 'Math', 'Physics', name= 'Bill', age=23)

courses = ['Science', 'Math', 'Physics']
info = {'name': 'Bill', 'age': 23}

student_info(*courses, **info)