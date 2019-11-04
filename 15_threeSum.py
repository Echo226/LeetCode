# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for cur in range(len(nums)):
            
            if nums[cur] > 0: break
            if cur>0 and nums[cur]==nums[cur-1]: continue   # 重点理解

            left = cur + 1
            right = len(nums) - 1
            
            while left < right:
                if nums[cur] + nums[left] + nums[right] > 0:
                    # while left < right and nums[right-1] == nums[right]:
                    #     right -= 1
                    right -= 1
                    
                elif nums[cur] + nums[left] + nums[right] < 0:
                    # while left < right and nums[left+1] == nums[left]:
                    #     left += 1
                    left += 1
                
                else:
                    res.append([nums[cur], nums[left], nums[right]])
                    print([nums[cur], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
                
            
