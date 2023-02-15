def MergedList1(*x):
    empty_list = []
    if len(x) < 2:
        return empty_list
    else:
        return sorted(list(x))

def MergedList2(*y):
    empty_list_1 = []
    if len(y) < 2:
        return empty_list_1.append(y)
    else:
        return sorted(list(y))

def Solution():
    if len(MergedList1()) > 2:
        merged = MergedList1() + MergedList2()
        print(sorted(merged))
    else:
        return None

MergedList1(1)
MergedList2(2, 7, 6, 9)
print(Solution())














