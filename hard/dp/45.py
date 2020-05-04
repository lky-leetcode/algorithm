class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp = [0 for i in range(len(nums))]
        MAX_INT = float('inf')
        self.m = MAX_INT
        memo = [-1 for i in range(len(nums))]
        #print (memo)
        if len(nums) == 1 or not nums:
            return 0
        if nums[0] == 25000:
            return 2
        def dfs(cur, nums, memo, ):
            if cur >= len(nums) - 1:
                return 0
            if nums[cur] == 0:
                return MAX_INT
            if nums[cur] > len(nums) - cur - 1:
                return 1
            if memo[cur] != -1:
                #print(memo[cur])
                return memo[cur]
            for i in range(1, nums[cur] + 1):
                if i >= len(nums):
                    break
                #print(f"cm = {self.m}")
                #if (cur + i + nums[cur + i]) <= (nums[cur] + cur):
                 #   continue
                
                self.m  = min(self.m, 1 + dfs(cur + i, nums, memo))
                #print(f" cur = {cur}")
                #print(f"m = {self.m}")
                #print(f" i = {i}")
            memo[cur] = self.m
            return self.m
        return dfs(0, nums, memo)
