def function(*nums):
    my_list = list(nums)
    for i in range(1, len(my_list)):
        my_list[i] += my_list[i-1]
    return my_list

print(function(1, 2, 3, 4))
