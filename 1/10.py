# wap to sum all the items in a list

def sum_list_max(arr):
    max = arr[0]
    total = 0;
    for item in arr:
        if(max<item):
            max = item;
        total += item
    return {total,max}

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("sum and max", sum_list_max(arr));

