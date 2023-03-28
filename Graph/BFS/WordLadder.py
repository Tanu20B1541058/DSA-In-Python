from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        s=set(wordList)
        l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']
        queue=deque([])
        queue.append([beginWord,0])
        while queue:
            a,b=queue.popleft()
            if a==endWord:
                return b+1
            for j in range(len(a)):
                for i in l:
                    if (a[:j]+i+a[j+1:]) in s and (a[:j]+i+a[j+1:])!=beginWord:
                        s.remove(a[:j]+i+a[j+1:])
                        queue.append([a[:j]+i+a[j+1:],b+1])
        return 0 