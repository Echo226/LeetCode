'''
  Method1: Brute Force
  Method2: Sort
  Method3: Hash-Table
  Method4: Boyer-Moore Algorithm
  Method5: Randomization
  Medhod6: Divide and Conquer
'''


# Brute Force
# Time Complexity: O(N^2) - Time Limit Exceeded
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num1 in nums:
            cnt = 0
            for num2 in nums:
                if num2 == num1:
                    cnt += 1
            if cnt > len(nums)//2:
                return num1

# Sort
# Time Complexity: O(NlogN)
# Space Complexity: O(1)/O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# Hash-Table
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for key, value in dic.items():
            if value > len(nums)//2:
                return key


# Boyer-Moore Algorithm
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            if num == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate
