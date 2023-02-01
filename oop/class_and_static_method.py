class Employee:
    
    raise_amount = 1.04
    no_of_employees = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@gmail.com'.format(self.first, self.last)
        
        Employee.no_of_employees += 1
        
    def apply_raise(self): # regular methods 
        self.pay = int(self.pay * self.raise_amount) 
          
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @classmethod
    def set_raise_amount(cls, amount): #class method recieves class(cls) rather than instance(self) 
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod  # static method, does not take any instance or class 
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Bill', 'John', 50000)
emp2 = Employee('John', 'Bill', 60000)

import datetime
my_date = datetime.date(2023,1,28)

print(Employee.is_work_day(my_date))


# if there is no need of cls and self inside the class and regular methods, we check if we can
#them static method






        