class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        freq = {}
        for ch in p:
            freq[ch] = freq.get(ch,0)+1

        ans = []
        count = len(freq)

        i=0
        j=0
        while(j<len(s)):
            #add charcter

            if s[j] in freq:
                freq[s[j]]-=1

                if freq[s[j]] ==0:
                    count -=1

            # window size

            if j-i+1 <n:
                j+=1

            elif j-i+1 == n:
                if count == 0:
                    ans.append(i)

                if s[i] in freq:
                    if freq[s[i]] == 0:
                        count+=1

                    freq[s[i]] +=1
                i+=1
                j+=1

        return ans            



        