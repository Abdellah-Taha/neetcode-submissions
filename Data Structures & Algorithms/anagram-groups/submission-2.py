class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s: dict = {}
        for key in strs:
            s.setdefault("".join(sorted(key)), []).append(key)
        return list(s.values())