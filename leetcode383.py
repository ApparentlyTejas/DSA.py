class solution:
    def forConstructor(self, ransomeNote: str, magazine: str) -> bool:
        for letter in ransomeNote:
            if letter in magazine:
                position = magazine.index(letter)
                magazine = magazine[:position] + magazine[position+1:]
            else: 
                return False
        return True
#time: O(m*n)
#space: O(1)

#optimal Solution:

from collections import Counter
class solution:
    def Constructor(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)
        for char in ransomNote:
            if hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                return False
        return True
#time: O(m+n)
#space: O(1)
