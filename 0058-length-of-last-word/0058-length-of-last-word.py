class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split()

        if words:
            return len(words[-1])
        else:
            return 0