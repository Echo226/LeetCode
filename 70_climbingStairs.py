'''
    Method1: Naive Recursion
    Method2: Memoization - Top_Dowm
    Method3: Memoization - Bottom_Up wilt Space Complexity O(N)
    Method4: Memoization - Bottom_Up with Space Complexity O(1)
    
    Author: Xinting
    Date  : 2019-11-14
'''


# Naive Recursion - Time Limit Exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            res = n
        else:
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
        return res
    
# Memoization - Top_Dowm
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbStairs_memo(n, memo)
    
    def climbStairs_memo(self, n, memo):
        if n in memo:
            return memo[n]
        if n <= 2:
            res = n
        else:
            res = self.climbStairs_memo(n-1, memo) + self.climbStairs_memo(n-2, memo)
        memo[n] = res
        return memo[n]

# Memoization - Bottom_Up wilt Space Complexity O(N)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
        
# Memoization - Bottom_Up with Space Complexity O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        memo = [1,2]
        for i in range(3, n+1):
            temp = memo[0] + memo[1]
            memo[0] = memo[1]
            memo[1] = temp
        return memo[1]
        
        
        
        
        
        
        
        
