class Solution(object):
    def predictTheWinner(self, nums):
        n =len(nums)

        dp = nums[:]
        for length in range(2,n+1):
            for i in range(n-length+1):
                j = i + length -1

                left = nums[i]-dp[i + 1]
                right = nums[j] -dp[i]

                dp[i] = max(left ,right)

        return dp[0] >= 0
        