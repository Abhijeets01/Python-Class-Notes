my_list = ['A string', 23, 100.232, 'o']
# print(my_list)


my_list_two = ['one', 'two', 'three', 4, 5]
result = my_list_two[2]
# print(result)


# append
num_list = [1, 2, 3]
num_list.append('Four')
# print(num_list)

# o/p =>[1, 2, 3, 'Four']

# pop
num_list.pop()
# print(num_list)
# [1, 3, 'Four']
# [1, 2, 3]


# sort

new_list = ['a', 'e', 'x', 'b', 'c']
new_list.sort()
# print(new_list)
# ['a', 'b', 'c', 'e', 'x']


# reverse
new_list.reverse()
# print(new_list)

# ['x', 'e', 'c', 'b', 'a']


# Data structures =>

# Nesting:
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

matrix = [list_1, list_2, list_3]
# print(matrix)

second_num_list = matrix[2][1]
# print(second_num_list)
