immutable_var = (1, 2, "String", True, 3.3, 'D')
print('tuple:', immutable_var)
# immutable_var[2] = 3
# print(immutable_var)

# Кортежи являются immutable:
#   1. Для хранения неизменяемого списка у которого тип 'tuple', а не 'list'
#   2. Для экономии памяти

mutable_list = [1, 2, "String", True, 3.3, 'D']
print('list:', mutable_list)
mutable_list[1] = "String"
mutable_list[2] = True
mutable_list[3] = 4
mutable_list[4] = 'D'
mutable_list[5] = 3.3
print('modified_list:', mutable_list)

print('size_tuple:', immutable_var.__sizeof__())
print('size_list:', mutable_list.__sizeof__())
