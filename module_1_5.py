immutable_var = (1, 3.4, 'Hello!', True)
print (immutable_var)
# immutable_var[2] = 'New [2]' так нельзя сделать из-за того, что кортежи -
# это неизменный список (константа)
mutable_list = [1, 3.4, 'Hellow!', True]
mutable_list[2] = 'New [2]'
print (mutable_list)