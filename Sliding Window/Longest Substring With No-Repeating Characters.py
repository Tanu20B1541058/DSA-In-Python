def longestSubstringWithNoDistinct(st):
    n = len(st)
    windowStart = 0
    length = 0
    # Store index of each character
    positionMap = {}
      
    for windowEnd in range(n):
        rightChar = st[windowEnd]
        if rightChar in positionMap:
            windowStart = max(windowStart, positionMap[rightChar] + 1)
        positionMap[rightChar] = windowEnd
        length = max(length, windowEnd - windowStart + 1)
    return length
s="pprrpsqqs"
print(longestSubstringWithNoDistinct(s))