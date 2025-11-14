def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            right = mid - 1
        else: 
            left = mid + 1

    return -1

print(find([2, 4, 8, 16, 20], 8))
