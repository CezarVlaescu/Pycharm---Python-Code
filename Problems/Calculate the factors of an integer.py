def calculate_factor(num):
    empty_list = []
    for i in range(1, num+1):
        if num % i == 0:
            empty_list.append(i)
    return empty_list

print(calculate_factor(30))

