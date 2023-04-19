class Solution:
    def lowerbound(self,a,array):
        low=0
        high=len(array)-1
        while(low<=high):
            mid=(low+high)//2
            if(a==array[mid]):
                return mid
            elif array[mid]>a:
                high=mid-1
            else:
                low=mid+1
        return low

            
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key=lambda pair:(pair[0],-pair[1]))
        array=[]
        array.append(envelopes[0][1])
        for i in range(1,len(envelopes)):
                if envelopes[i][1]>array[len(array)-1]:
                    array.append(envelopes[i][1])
                else:
                    a=self.lowerbound(envelopes[i][1],array)
                    array[a]=envelopes[i][1]
        return len(array)