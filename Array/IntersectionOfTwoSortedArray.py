a = [1, 2, 2, 3, 3, 4, 5, 6]
b = [2, 3, 3, 5, 6, 6, 7]
i , j = 0, 0
n = len(a)
m = len(b)
ans = []
while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif b[j] < a[i]:
        j += 1
    else:
        ans.append(a[i])
        i += 1
        j += 1
print(ans)

#TC ---> O(N1 + N2)
# SC ---> O(1)