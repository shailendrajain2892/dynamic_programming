def rob(arr, n) -> int:
    if n == 0: 
        return 0
    if n == 1:
        return arr[n-1]
    if n==2:
        return max(arr[n-1], arr[n-2])
    return max(arr[n-1]+rob(arr, n-2), rob(arr, n-1))

print(rob([1, 9, 2, 2, 7, 1], 6))

