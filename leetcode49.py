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