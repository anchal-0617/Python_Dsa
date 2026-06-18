class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        freq = {}

        max_length = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1

            max_freq = max(max_freq, freq[s[right]])

            length = right-left+1

            while length - max_freq > k:

                freq[s[left]] -= 1
                left+=1

                length = right-left+1
            max_length = max(max_length , length)
        return max_length




