# wap to sum all the items in a list

def sum_list(arr):
    total = 0;
    for item in arr:
        total += item
    return total

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("sum", sum_list(arr))
