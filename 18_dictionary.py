my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))
# <class 'dict'>
print(my_dictionary[3])
# 9

my_dictionary[9] = 81
print(my_dictionary)
# {5: 25, 2: 4, 3: 9, 9: 81}

my_otter = {
    'mother_otter': '수마',
    'father_otter': '수빠',
    'son_otter': '수달',
}
print(my_otter['son_otter'])
# 수달

print("---------------")

print(my_otter.values())
# dict_values(['수마', '수빠', '수달'])

print('수달' in my_otter.values())
# True

print('해달' in my_otter.values())
# False

for value in my_otter.values():
    print(value)
# 수마
# 수빠
# 수달

print(my_otter.keys())
# dict_keys(['mother_otter', 'father_otter', 'son_otter'])

for key in my_otter.keys():
    print(key)
# mother_otter
# father_otter
# son_otter

for key in my_otter.keys():
    value = my_otter[key]
    print(key, value)
# mother_otter 수마
# father_otter 수빠
# son_otter 수달

print(my_otter.items())
# dict_items([('mother_otter', '수마'), ('father_otter', '수빠'), ('son_otter', '수달')])

for key, value in my_otter.items():
    print(key, value)
# mother_otter 수마
# father_otter 수빠
# son_otter 수달