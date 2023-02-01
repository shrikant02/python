class Employee:
    
    raise_amount = 1.04
    no_of_employees = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@gmail.com'.format(self.first, self.last)
        
        Employee.no_of_employees += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount) # class variable, accessed using class name
        self.pay = int(self.pay * self.raise_amount)
        
        
emp1 = Employee('Bill', 'John', 50000)
emp2 = Employee('John', 'Bill', 60000)
emp3 = Employee('Jack', 'Johnson', 50000)

emp1.raise_amount = 1.05

emp1.apply_raise()
print(emp1.pay)

emp3.apply_raise()
print(emp3.pay)
        