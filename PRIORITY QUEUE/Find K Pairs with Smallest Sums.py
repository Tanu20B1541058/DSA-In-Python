from heapq import *
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        max_heap, result = [], []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                sum_val = nums1[i] + nums2[j]
                if len(max_heap) < k:
                    heappush(max_heap, (-sum_val, i, j))
                else:
                    if sum_val > -max_heap[0][0]:
                        break
                    else:
                        heappushpop(max_heap, (-sum_val, i, j))
        
        for _, i, j in max_heap:
            result.append([nums1[i], nums2[j]])
        
        return result
