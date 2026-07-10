class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha1= {}
        alpha2 = {}
        for letter in  s:
            alpha1[letter] = alpha1.get(letter, 0) + 1
        
        for letter in  t:
            alpha2[letter] = alpha2.get(letter, 0) + 1
        
        return alpha1 == alpha2

print(Solution().isAnagram("racecar", "carrace"))