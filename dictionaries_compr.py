#Dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#print (zip(names, heros))

#I want a dict{'name': 'hero'} for each name, hero in zip(name, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

#I want a dict{'name': 'hero'} for each name, hero in zip(name, heros)
#As a dictionary comprehension
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

#If name is not equal to Peter
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

#Set Comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

#Using set comprehensions
my_set = {n for n in nums}
print(my_set)

#Generator Expressions
#I want to yield 'n * n' for 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''def get_func(nums):
    for n in nums:
        yield n * n
        '''
#Using generator comprehensions
my_gen = (n*n for n in nums)

#my_gen = get_func(nums)
for i in my_gen:
    print(i)