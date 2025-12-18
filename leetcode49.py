from collections import defaultdict
class solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)- ord('a')] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())
    
#time: O(m*n) space: O(m*n)


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            hashmap[tuple(count)].append(s)

        return list(hashmap.values())