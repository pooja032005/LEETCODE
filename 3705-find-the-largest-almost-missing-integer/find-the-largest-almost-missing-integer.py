class Solution(object):
    def largestInteger(self, nums, k):
        count ={}

        n = len(nums)
        
        for i  in range(n-k+1):
            seen =set()

            for j in range(i,i+k):
                seen.add(nums[j])

            for num in seen:
                count[num] = count.get(num,0)+1

        answer = -1

        for num in count:
            if count[num] == 1:
                answer = max(answer,num)

        return answer
        