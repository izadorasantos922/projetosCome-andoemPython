class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1:
                num-=1
            else:
                num>>=1
            steps+=1
        return steps
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        for i in range(len(nums)+1):
            x ^= i

        return x