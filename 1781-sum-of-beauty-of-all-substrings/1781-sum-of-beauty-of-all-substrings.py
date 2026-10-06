class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0

        n = len(s)

        for i in range(n):
            freq = [0]*26

            for j  in range(i,n):

                freq[ord(s[j]) - ord('a')] += 1

                max_freq = max(freq)

                # min_freq = min(x for x in freq if x>0)


                min_freq = float('inf')

                for x in freq:
                    if x>0:
                        min_freq = min(min_freq , x)

                ans += max_freq - min_freq

        return ans        

        