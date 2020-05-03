class Solution:
    def maxSubArray(self, nums):
        dp = []
        M = nums[0]
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i] , nums[i]))
            if (dp[i] > M):
                M = dp[i]
        return M
        
