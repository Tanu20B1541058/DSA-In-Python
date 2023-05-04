# Brute Force solution
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
temp = []
for i in range(len(arr)):
    if arr[i] != 0:
        temp.append(arr[i])
idx = 0
for i in temp:
    arr[idx] = i
    idx += 1
for i in range(len(temp),len(arr)):
    arr[i] = 0
print(arr)

# TC --> O(2N)
# SC --> O(N)

# Optimal Solution
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
j = -1
for i in range(len(arr)):
    if arr[i] == 0:
        j = i
        break


for i in range(j+1, len(arr)):
    if arr[i] != 0:
        arr[i] , arr[j] = arr[j] , arr[i]
        j += 1
print(arr)

# TC --> O(2N)
# SC --> O(1)


