# Brute force technique

arr = [3, 2, 1, 5, 2]
arr.sort()
print(arr[-1])

# Time Complexity ---> O(nlogn)
# Space Complexity ---> O(1)

# Optimal Solution

arr = [3, 2, 1, 5, 2]
largest = arr[0]
for i in range(1, len(arr)):
    if largest < arr[i]:
        largest = arr[i]
print(largest)

# Time Complexity ---> O(n)

