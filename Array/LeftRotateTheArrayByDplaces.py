# Brute foece
arr = [1,2, 3, 4, 5, 6, 7, 8]
d = 3
temp = []
for i in range(d):
    temp.append(arr[i])
# shifting
n = len(arr)
for i in range(d,n):
    arr[i-d] = arr[i]
# put back temp
j = 0 
for i in range(n-d,n):
    arr[i] = temp[j]
    j += 1
print(arr)

# TC --> O(d) + O(n-d) + O(d)
# SC --> O(d)

# OPTIMAL Solution
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 3
def reverse(num):
    return num[::-1]
arr[:3] = reverse(arr[:3])
arr[3:] = reverse(arr[3:])
arr = reverse(arr)
print(arr)

# TC --> O(2N)
# SC --> O(1)

