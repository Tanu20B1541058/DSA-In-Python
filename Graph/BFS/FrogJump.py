class Solution:
    @staticmethod
    def canCross(stones):
        n=stones[len(stones)-1]
        if stones[1] !=1:
            return False
        map=dict()
        for s in stones:
            map[s]=set()
        map[stones[0]].add(1)
        for pos in stones:
            jumps=map[pos]
            for j in jumps:
                n_pos= pos+j
                if n_pos == n:
                    return True
                if n_pos in map:
                    if j-1 >0:
                        map[n_pos].add(j-1) 
                    map[n_pos].add(j)
                    map[n_pos].add(j+1)
        return False
if __name__ == '__main__':
    stones = [0,1,3,5,6,8,12,17]
    print(Solution.canCross(stones))
