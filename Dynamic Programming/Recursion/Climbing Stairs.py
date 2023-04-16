def solve(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        left=solve(n-1)
        right=solve(n-2)
        return left+right
n=3
print(solve(n))