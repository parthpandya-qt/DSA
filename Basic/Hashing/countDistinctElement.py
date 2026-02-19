def distinct(arr):
    count = 0
    for i in range(len(arr)):
        is_unique = True
        for j in range(i):
            if arr[i] == arr[j]:
                is_unique = False
                break
        if is_unique:
            count += 1
    return count

# Example usage:
print(distinct([1, 2, 2, 3, 4, 4, 5]))  # Output: 5