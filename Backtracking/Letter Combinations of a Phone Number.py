
def letterCombinations(digits):
    sub=[]
    combination=[]
    dic = { 2: "abc", 3: "def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    if len(digits)<1:
        return []

    def solve(index,digits,sub,combination,dic):
        if len(sub) ==len(digits):
            st=sub.copy()
            combination.append(''.join(st))
            return
        if (index==len(digits)):
            return
        button=dic[int(digits[index])]
        for i in range(len(button)):
            sub.append(button[i])
            solve(index+1,digits,sub,combination,dic)
            sub.remove(button[i])
    solve(0,digits,sub,combination,dic)
    return combination
digits="23"
print(letterCombinations(digits))