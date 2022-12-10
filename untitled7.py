
with open('test2.txt', 'w') as f:
    f.write("Test 2")
    
    
with open('file.txt', 'r') as rf:
    with open('file_copy.txt', 'w') as wf:
        chunk_size = 10
        
        chunk = rf.read(chunk_size)
        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(chunk_size)
            
            
