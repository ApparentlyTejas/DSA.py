from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val , key))
            else:
                heapq.heappushpop(heap, (val, key))


        return [h[1] for h in heap]
    
# Time: O( N log K)
# Space: O(n)