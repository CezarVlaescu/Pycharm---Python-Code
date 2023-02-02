my_dict = {'a': 2, 'b': {'c': [1, 2, 3]}, 'd': [1, 2, [3, 4, 5]]}
var = my_dict['b']
var1 = my_dict['b']['c'][1]
var2 = my_dict['d'][2][1] # print from dict
my_dict['e'] = 3 # add in dict
my_dict['a'] = 4 # reread an element from dict
print(my_dict)
print(my_dict.keys()) # print keys
print(my_dict.values()) # print values
print(my_dict.items()) # print all 