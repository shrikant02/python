nums = [1,2,3,4,5,6,7,8,9,10,2,5,1,8,4,3]

my_list = [n*n for n in nums]

even = [n for n in nums if n%2 == 0]


# =============================================================================
# for i in 'abcd':
#     for num in range(4):
#         my_list_2.append((i,num))
# =============================================================================

my_list_2 = [(letter, num) for letter in 'abcd' for num in range(4)]

#print(my_list_2)

names = ['Bruce','Clark','Peter','Logan','Wade']
heroes = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

# =============================================================================
# my_dic = {}
# 
# for name, hero in zip(names, heroes):
#     my_dic[name] = hero
# =============================================================================

my_dic = {name: hero for name, hero in zip(names, heroes)}

my_set = {n for n in nums}

print(my_set)



        
