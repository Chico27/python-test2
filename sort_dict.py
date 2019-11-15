from collections import OrderedDict

num_eng = {'5': 'five', '1': 'one', '7': 'seven', '3':  'three'}

print('')
print(num_eng)
print(type(num_eng))

sorted_num_eng = sorted(num_eng.items())

print('')
print(sorted_num_eng)
print(type(sorted_num_eng))

sorted_num_eng = OrderedDict(sorted_num_eng)

print('')
print(sorted_num_eng)
print(type(sorted_num_eng))

print(sorted_num_eng['5'])
