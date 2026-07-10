class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        n = len(s)
        if s[:n] != s[::-1]:
            return False
        return True