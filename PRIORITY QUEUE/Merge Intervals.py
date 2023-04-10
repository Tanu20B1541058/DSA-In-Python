class MergeIntervals:
    
    @staticmethod
    def mergeIntervals(intervals):
        intervals.sort(key=lambda x:x[0])
        
        merge_interval=[]
        prev_interval=intervals[0]
        
        if len(intervals)<2:
            return intervals
        else:
            for i in range(1,len(intervals)):
                interval=intervals[i]
                
                if interval[0]<=prev_interval[1]:
                    prev_interval[1]=max(prev_interval[1],interval[1])
                else:
                    merge_interval.append(prev_interval)
                    prev_interval=interval
            
            merge_interval.append(prev_interval)
            return merge_interval

if __name__=='__main__':
    intervals = [[1, 4], [2, 5], [7, 9]]
    for i in MergeIntervals.mergeIntervals(intervals):
        print(i, end = " ")
    
                
                