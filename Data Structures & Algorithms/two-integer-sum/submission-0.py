class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in s:
                return [s[diff], i]
            else:
                s[num] = i
        return []
                
        