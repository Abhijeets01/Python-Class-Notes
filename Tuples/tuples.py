# Tuples
tup_1 = (1, 2, 3)
tup_2 = ('Abhijeet', 'Sharma', 1, 2, 3, 4, 5)
# print(tup_1)
# print(len(tup_1))
# print(tup_2[1])
# (1, 2, 3)
# ('Abhijeet', 'Sharma')

# tup_1[0] = 5
# print(tup_1)

# Sets
myset = {"apple", "banana", "cherry", 1, 2, 3, 4}
# print(myset)

thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)
thisset.add("orange")
thisset.add(1)
# print(thisset)


list1 = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
remove_duplicate = set(list1)
# print(remove_duplicate)


# 0 => False
# 1 => True

# print(1 > 3)
# print(4 > 3)


# Comparison Operators
a = 3
b = 4

print(a == b)

# ! = > not

print(a != b)

# Chain Operators

c = 1 < 3 and 1 > 2 < 3
print(c)

d = 1 == 2 or 2 < 3
print(d)

e = 1 < 2 < 3
print(e)
