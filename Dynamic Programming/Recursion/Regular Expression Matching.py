class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def check(p,n):
            for i in range(n-1, -1, -2):
                if p[i] != '*':
                    return False
            return True 
        def solve(s, p, m, n):
            if m == 0 and n == 0:
                return True
            if n == 0:
                return False
            if m == 0 and check(p, n):
                return True
            if m == 0:
                return False
            if s[m-1] == p[n-1] or p[n-1] == '.':
                return solve(s, p, m-1, n-1)
            if p[n-1] == '*':
                if p[n-2] == ".":
                    flag = False
                    for i in range(m+1):
                        flag = flag or solve(s,p, m-i, n-2)
                        if flag:
                            return True
                    return flag
                else:
                    flag = False
                    for i in range(m+1):
                        if i == 0:
                            flag = flag or solve(s, p, m-i, n-2)
                            if flag :
                                return True
                        else:
                            if s[m-i] == p[n-2]:
                                flag = flag or solve(s, p, m-i, n-2)
                                if flag :
                                    return True
                            else:
                                return False
        return solve(s, p, len(s), len(p))


                        
                    

            

        