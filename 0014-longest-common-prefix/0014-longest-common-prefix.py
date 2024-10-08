class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]
        common_prefix_length = 0

        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                common_prefix_length += 1
            else:
                break

        return first_str[:common_prefix_length]