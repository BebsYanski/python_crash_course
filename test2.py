my_list = [1, 2, 3, 4, 5]
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] % 2 == 0]
even = [x for x in my_list if x % 2 == 0]
more_list = [my_list] * 3
my_list.append(6)
print(more_list)
print(new_list)
print((54).__add__(22))
print(dir(6))