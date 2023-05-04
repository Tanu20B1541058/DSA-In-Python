# Brute Force solution
arr = [1, 1, 2, 2, 2, 3, 3]
s = set()
for i in arr:
    s.add(i)

idx = 0
for i in s:
    arr[idx] = i
    idx += 1
print(arr)

# TC ---> O(nlogn) + O(n)
# SC --> O(N)

# Optimal Solution (2 Pointers)

i = 0
for j in range(len(arr)):
    if arr[j] != arr[i]:
        arr[i+1] = arr[j]
        i += 1
print(i+1)

# TC ---> O(n)
# SC ---> O(1)



