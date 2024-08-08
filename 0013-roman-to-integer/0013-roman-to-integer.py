class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        n = len(s)

        for i in range(n-1):
            current_val = roman_to_int_map[s[i]]
            next_val = roman_to_int_map[s[i+1]]

            if current_val < next_val:
                total -= current_val

            else:
                total += current_val

        total += roman_to_int_map[s[-1]]
        return total