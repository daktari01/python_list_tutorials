nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

#Using list comprehensions: 
#I want 'n' for each 'n' in nums
my_list = [n for n in nums]
print(my_list)

#***********************
#I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

#Using list comprehensions: 
#I want 'n*n' for each 'n' in nums
my_list = [n*n for n in nums]
print(my_list)

#Using map + lambda
#I want 'n*n' for each 'n' in nums
my_list = map(lambda n: n*n, nums)
print(my_list)

'''
Using map and lambda is however not
very readable, compared to using list
comprehensions
'''
#*********************
#I want 'n' for each 'n'in nums if each 'n' is even
my_list = []
for n in nums:
    if n % 2 ==0:
        my_list.append(n)
print (my_list)

#Using list comprehensions: 
#I want 'n' for each 'n'in nums if each 'n' is even
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

#Using filter + lambda 
#I want 'n' for each 'n'in nums if each 'n' is even
my_list = filter(lambda n: n % 2 == 0, nums)
print(my_list)

'''
Just like map and lambda, filter and lambda is also not
very readable, compared to using list
comprehensions
'''

#***************
#I want a (letter, num) pair for each letter in 'abcd' and --
#each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)
print("*********")
#Using list comprehensions
#I want a (letter, num) pair for each letter in 'abcd' and --
#each number in '0123'
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)