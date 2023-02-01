class Employee:
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@gmail.com'.format(self.first, self.last)
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amount)
        

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
        

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None): # employees=None is defualt value
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        
        
dev_1 = Developer('Bill', 'John', 50000, 'Python')
dev_2 = Developer('John', 'Bill', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.print_emp()

#print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Employee))