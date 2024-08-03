class Solution:
    def largestOddNumber(self, num: str) -> str:
        largest_odd = ""
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                largest_odd = num[:i + 1]

        return largest_odd