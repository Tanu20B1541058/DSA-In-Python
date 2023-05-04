# Brute Force Solution 
arr = [1, 2, 4, 7, 7, 5]
arr.sort()
print(arr[-2])

# Better Solution
arr = [1, 2, 4, 7, 7, 5]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
second_largest = -1     # if element is positive integer
for i in range(len(arr)):
    if arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
print(second_largest)

# TC ---> O(n) + O(n)

# Optimal Solution
largest = arr[0]
second_largest = -1
for i in range(1,len(arr)):
    if largest < arr[i] :
        second_largest = largest 
        largest = arr[i]
    elif arr[i] < largest and arr[i] > second_largest:
        second_largest  = arr[i]
print(second_largest)

# Tc ---> O(n)


