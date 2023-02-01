class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        


emp1 = Employee('Bill', 'John', 50000) # emp1 will be passed in as self and it will set all the values.
emp2 = Employee('John', 'Bill', 60000) # similar

# print(emp1)
# print(emp2)

print(emp1.email)
print(emp2.email)

print(emp2.fullname())

Employee.fullname(emp1)  # calling the function by class, we need to instance 

#print('{} {}'.format(emp1.first, emp1.last))


# if we want to keep the class empty withour getting error for the time being we can use pass keyword

# __init__ => recieves the instance of the class(self, we can name it whatever we want), this method is 
# to initialize class instance, it is like contructor

# emp1.fullname() is transform into Employee.fullname(emp1) where emp1 is used as self instance.

# first, last, email and pay are the instance variable which we are unique to each instance.

# class methods automatically takes in instance, which we call instance.