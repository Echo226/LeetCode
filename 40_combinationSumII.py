# Backtracking with Pruning
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtracking(nums, [], target, 0, res)
        return res
        
    def backtracking(self, nums, tempList, remain, startIndex, res):
        if remain == 0:
            res.append(tempList[:])
            return
        
        for i in range(startIndex, len(nums)):
            # Avoid Duplicates, very important especially i>startIndex
            if i > startIndex and nums[i] == nums[i-1]:
                continue
            # Pruning
            if remain - nums[i] < 0: 
                break
            tempList.append(nums[i])
            self.backtracking(nums, tempList, remain-nums[i], i+1, res)   # i+1
            tempList.pop()
