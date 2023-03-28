def letterCasePermutation(s):
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)
                
        res = []
        backtrack()
        return res
s = "a1b2"
print(letterCasePermutation(s))