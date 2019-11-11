# Backtracking without Pruning
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtracking(nums, [], target, 0, res)
        return res
    
    def backtracking(self, nums, tempList, remain, startIndex, res):
        if remain == 0:
            res.append(tempList[:])
            return
        if remain < 0:
            return
        for i in range(startIndex, len(nums)):
            tempList.append(nums[i])
            self.backtracking(nums, tempList, remain - nums[i], i, res)
            tempList.pop()



# Backtracking with Pruning
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtracking(nums, [], target, 0, res)
        return res
    
    def backtracking(self, nums, tempList, remain, startIndex, res):
        if remain == 0:
            res.append(tempList[:])
            return      # If there is a break in pruning, this return can be deleted actually
        for i in range(startIndex, len(nums)):
            if remain - nums[i] < 0:                # Pruning
                break
            tempList.append(nums[i])
            self.backtracking(nums, tempList, remain - nums[i], i, res)
            tempList.pop()
