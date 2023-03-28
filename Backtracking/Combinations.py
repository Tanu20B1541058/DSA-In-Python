def combine(n, k):
        sol=[]
        def backtrack(k,comb,nex):
		
            if k==0:
                sol.append(comb.copy())
            else:
				
                for i in range(nex,n+1):
					# add candidate
                    comb.append(i)
					#backtrack
                    backtrack(k-1,comb,i+1)
					# remove candidate
                    comb.pop()
            
        backtrack(k,[],1)
        return sol
n = 4
k = 2
print(combine(n, k))