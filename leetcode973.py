import heapq
class Solution:
    def kClosest(self, points: list[int], k: int) -> list[list[int]]:
        def distance(x, y):
            return x**2 + y**2

        heap = []
        for x, y in points:
            d = distance(x, y)

            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else:
                heapq.heappushpop(heap, (-d, x, y))
        return [(x,y) for d , x, y in heap]
    
# Time: O( n log k)
# Space: O(k)