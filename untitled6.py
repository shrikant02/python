
# file = open('file.txt', 'r') 

# print(file.name) #name of the file
# print(file.mode)

# file.close()


# with open('file.txt') as f: # f is the variable
#     f_contents = f.read(100)
#     print(f_contents)
    
#     f_contents = f.read(100)
#     print(f_contents)
    
    
# with open('file.txt') as f:
#     for line in f:
#         print(line, end='')

# with open('file.txt') as f:
    
#     size_to_read = 10
    
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)
        
        
with open('file.txt') as f:
    
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    
    f.seek(0) # it set our position back to the beginning of the file
    
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    
    


