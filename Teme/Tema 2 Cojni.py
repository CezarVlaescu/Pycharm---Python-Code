def my_function(*args):
    s = 0
    for i in args:
        if int(i) == i:
            s = s + i
    print(s)

my_list = [1, 5, -3, "abc", [12, 56, "cad"]]
print(my_function(my_list))

