# Brute Force Solution
a = [1, 1, 2, 3, 4, 5]
b = [2, 3, 4, 4, 5]
s = set()
union = []
for i in range(len(a)):
    s.add(a[i])
for i in range(len(b)):
    s.add(b[i])
for i in s:
    union.append(i)
print(union)


# TC --> O(n1logn + n2logn) + O(n1+n2)
# SC --> O(n1 + n2) + O(n1+n2)

# Optimal Solution
a = [1, 1, 2, 3, 4, 5]
b = [2, 3, 4, 4, 5]
n1 = len(a)
n2 = len(b)
i, j = 0 , 0
union = []
while i < n1 and j < n2 :
    if a[i] <= b[j]:
        if len(union) == 0 or union[-1] != a[i]  :
            union.append(a[i])
        i += 1
    else:
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1
while i < n1:
    if len(union) == 0 or union[-1] != a[i]  :
        union.append(a[i])
    i += 1
while j < n2:
    if len(union) == 0 or union[-1] != b[j]:
        union.append(b[j])
    j += 1
print(union)

# TC ---> O(n1 + n2)
# SC ---> O(n1 + n2)





