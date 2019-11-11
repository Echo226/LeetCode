'''
    Method1: Brute Force
    Method2: Boyer-Moore Algorithm
    
    Author: Xinting
    Date  : 2019-11-04
'''


# Brute Force
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        for num1 in nums:
            if num1 not in res and sum(1 for num2 in nums if num2 == num1) > len(nums)//3:
                res.append(num1)
        return res

# Boyer-Moore Algorithm
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        cnt1, cnt2 = 0, 0
        candidate1, candidate2 = 0, 0
        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candidate2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
 
        # check two potential candidates
        if sum(1 for num in nums if num == candidate1) > len(nums)//3:
            res.append(candidate1)
        # for [0,0,0] candidate1=candidate2=0 so that need to make sure candidate2 not in res
        if candidate2 not in res and sum(1 for num in nums if num == candidate2) > len(nums)//3:
            res.append(candidate2)
        
        return res
        
