lst = [1, 1, 2, 2, 3, 3]

my_set = set()
for item in lst:
    if lst.count(item) != 1:
        my_set.add(item)
my_list = (list(my_set))
print(str(my_list))
