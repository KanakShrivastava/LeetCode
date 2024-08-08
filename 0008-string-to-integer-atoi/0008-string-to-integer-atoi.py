class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
            
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:
            s = s[1:]
        print(s)  # This will print the string after removing the sign character if present

        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

            # Check for overflow
            if sign == 1 and result >= 2**31:
                return 2**31 - 1
            if sign == -1 and result > 2**31:
                return -2**31

        return sign * result

# Example usage
# sol = Solution()
# print(sol.myAtoi("   -042"))  # Output should be -42
