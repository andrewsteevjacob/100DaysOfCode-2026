def largest_element(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = [3, 7, 9, 2, 5]
print(largest_element(arr))
