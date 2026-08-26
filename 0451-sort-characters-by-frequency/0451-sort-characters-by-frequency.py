class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        

        mp = {}

        for ch in s:

            mp[ch] = mp.get(ch,0)+1

        arr = sorted(mp.items() , key = lambda x:x[1] , reverse = True)

        ans = ""

        for ch , freq in arr:

            ans += ch * freq

        return ans       