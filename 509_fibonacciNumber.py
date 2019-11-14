'''
    Method1: Naive Recurison
    Method2: Memoization - Top_Down
    Method3: Memoization - Bottom_up with Space Complexity O(N)
    Method4: Memoization - Bottom_up with Space Complexity O(1)
''''

# Naive Recursion
# Time Complexity: O(2^N)
# Space Complexity: O(N)
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            result = N
        else:
            result = self.fib(N-1) + self.fib(N-2)
        return result


# Memoization - Top_Down
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def fib(self, N: int) -> int:
        memo = {}
        return self.fib_memo(N, memo)

    def fib_memo(self, N, memo):
        if N in memo:
            return memo[N]
        if N <= 1:
            result = N
        else:
            result = self.fib_memo(N-1, memo) + self.fib_memo(N-2, memo)
        memo[N] = result
        return result
    
    
# Memoization - Bottom_Up
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def fib(self, N: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        for i in range(2, N+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[N]
        

# Memoization - Bottom_Up
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        memo = [0,1]
        for i in range(2, N+1):
            temp = memo[0] + memo[1]
            memo[0] = memo[1]
            memo[1] = temp
            
        return memo[1]
