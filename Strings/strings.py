# '=' assignment in programming

statement = 'Now I "ready" to use the single quotes inside a string!'
# print(len(statement))

# \n => backward slash and n => newline

var = 'He"llo'
len_var = len(var)
# print(len_var)


# Indexing
first_name = 'Abhijeet'
result = first_name[2]
# print(result)

str = 'Hello'
str_result = str[4]
# print(str_result)


name = 'Abhijeet'
name_res = name[4:6]
# print(name_res)


s = 'Hello World'
str_res = s[:3]
# print(str_res)
# ello World
# Hel

str = 'Hello World'
# str[0] = 'x'
# print(str)

str_result = str + ' concatenate me!'
# print(str_result)
# print(str)

# Methods
str = 'Hello World'
str_upper = str.upper()
# print(str_upper)

str_lower = str.lower()
# print(str_lower)

str_split = str.split()
# print(str_split)
# ['Hello', 'World']


my_name = 'Abhijeet'
print('Hello ' + my_name)


player = 'Thomas'
points = 33

# string formatting

str_formatting = f'Last night, {player} scored {points} points.'
print(str_formatting)
print(f'Last night {my_name} scored {points} points')
