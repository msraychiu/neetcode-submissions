class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        
        heap = [(-value, key) for key, value in count_map.items()]
        heapq.heapify(heap)

        result = []
        for i in range(k):
            v, k = heapq.heappop(heap)
            result.append(k)

        return result
