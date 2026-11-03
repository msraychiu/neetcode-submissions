class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 

        distinct = set(nums)
        sort = sorted(distinct)
        result = 0

        j = 1
        tmp = 1
        while j < len(sort):
            if sort[j] - sort[j-1] == 1:
                tmp += 1
            else:
                result = max(result, tmp)
                tmp = 1
            j += 1
        
        result = max(result, tmp)

        return result
            
