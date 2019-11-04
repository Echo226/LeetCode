# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
# Two-pass Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            implement = target - nums[i]
            if implement in dic and i != dic[implement]:
                return [i, dic[implement]]
                
# One-pass Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            implement = target - nums[i]
            if implement not in dic:
                dic[nums[i]] = i
            else:
                return [i, dic[implement]]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):    # enumerate
            implement = target - num
            if implement not in dic:
                dic[num] = i
            else:
                return [i, dic[implement]]
