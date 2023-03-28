def generateParenthesis(n):
        output=''
        ans=[]

        def solve(op,cl,output,ans):
            if op==0 and cl==0:
                ans.append(output)
                return
            
            if op !=0 and cl>op:
                solve(op-1,cl,output+'(',ans)
                solve(op,cl-1,output+')',ans)
            else:
                if op==0:
                    solve(op,cl-1,output+')',ans)
                if op ==cl:
                    solve(op-1,cl,output+'(',ans)
        solve(n,n,output,ans)
        return ans
n=3
print(generateParenthesis(n))