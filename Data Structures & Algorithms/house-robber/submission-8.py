class Solution:
    def rob(self, nums: List[int]) -> int:  

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        money = [-1] * n

        def dp(index):
            if index == 0 or index == 1:
                money[index] = nums[index]
                return money[index]
            if money[index] != -1:
                return money[index]
            max_money = dp(index - 1)
            for i in range(0, index - 1):
                max_money = max(max_money, dp(i) + nums[index])
            money[index] = max_money
            return money[index]
    
        dp(n - 1)
        return max(money[n - 1], money[n - 2])            
            
