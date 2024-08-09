class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        closed_needed = 0

        for char in s:
            if char == "(":
                closed_needed += 1
            elif char == ")":
                if closed_needed > 0:
                    closed_needed -= 1
                else:
                    open_needed += 1
        return open_needed + closed_needed