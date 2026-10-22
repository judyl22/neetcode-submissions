class Solution:
    def rob(self, nums: List[int]) -> int:  

        n = len(nums)
        money = [-1] * n

        def dp(index):
            if index == 0:
                money[0] = nums[0]
                return money[0]
            if index == 1:
                money[1] = max(nums[1], nums[0])
            if money[index] != -1:
                return money[index]
            max_money = max(dp(index - 1), dp(index - 2) + nums[index])
            money[index] = max_money
            return money[index]
    
        dp(n - 1)
        return max(money[n - 1], money[n - 2])            
            
