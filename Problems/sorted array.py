def sort(arr, n):
    i = 0
    while (i < n):
        correct = arr[i] - 1

        if arr[correct] != arr[i]:
            swap(arr, i, correct)
        else:
            i = i + 1

def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

arr = [3, 2, 5, 6, 1, 4]
n = len(arr)
sort(arr, n)
for i in range(0, n):
    print(arr[i], end=" ")