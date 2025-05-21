class solution:
    def forConstructor(self, ransomeNote: str, magazine: str) -> bool:
        for letter in ransomeNote:
            if letter in magazine:
                position = magazine.index(letter)
                magazine = magazine[:position] + magazine[position+1:]
            else: 
                return False
        return True