class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            target = 0 - num
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target:
                    temp = sorted([num, nums[j], nums[k]])
                    if temp not in result:
                        result.append(sorted([num, nums[j], nums[k]]))
                    j+=1
                elif  nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return result
        