import datetime

greeting = "Hello"
name = "Bill"

message = greeting + ", " + name + ". Welcome!"

message_2 = '{}, {}. Welcome!'.format(greeting, name)

message_3 = f'{greeting}, {name}. Welcome!'

message_4 = f'{greeting}, {name.upper()}. Welcome!'


#print(dir(name)) # will give all the available function with the variable.

print(help(str.lower))

print(datetime.datetime(2022,12,1, 12, 34, 10))







