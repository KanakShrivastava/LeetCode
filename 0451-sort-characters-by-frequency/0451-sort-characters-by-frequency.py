class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)

        sorted_chars = frequency.most_common()

        result = ''.join([char * count for char, count in sorted_chars])

        return result