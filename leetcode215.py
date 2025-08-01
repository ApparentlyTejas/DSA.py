import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap , num)

            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
    
# Time: O(n log K)

# Space: O(K)