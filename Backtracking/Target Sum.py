def findTargetSumWays(nums, target) :
        def backtrack(total, index, memo):
            # base case
            if (index, total) in memo:
                return memo[(index, total)]
            
            if total == target and index == len(nums):
                return 1
            elif index >= len(nums):
                return 0

            
            answer = 0
            
            answer += backtrack(total + nums[index], index + 1, memo)
            

            
            answer += backtrack(total - nums[index], index + 1, memo)
            

            memo[(index, total)] = answer
            
            return memo[(index, total)]

        return backtrack(0, 0, {})
nums = [1,1,1,1,1] 
target = 3
print(findTargetSumWays(nums, target))