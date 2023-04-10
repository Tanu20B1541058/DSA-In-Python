import sys
 
def toysIntoBags(toys):
    n = len(toys)
    windowStart = 0
    length = -sys.maxsize-1
    # Store count of characters
    frequencyMap = {}
     
    for windowEnd in range(n):
        rightChar = toys[windowEnd]
        if rightChar in frequencyMap:
            frequencyMap[rightChar] += 1
        else:
            frequencyMap[rightChar] = 1
         
        while len(frequencyMap) > 2:
            leftChar = toys[windowStart]
            frequencyMap[leftChar] -= 1
            if frequencyMap[leftChar] == 0:
                del frequencyMap[leftChar]
            windowStart += 1
        length = max(length, windowEnd - windowStart + 1)
    return length
     
if __name__ == "__main__":
    print(toysIntoBags(['A', 'R', 'A', 'A', 'B', 'D', 'D', 'A']))
    print(toysIntoBags(['A', 'C', 'I', 'A', 'C', 'I', 'I']))