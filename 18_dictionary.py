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