#time: O(m *n)
class solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
    
#better solution with time: O(m+n) 
#space: O(n)
class solution:
    def numJewelsInStones(self, jewels: str, stones: str)-> int:
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count