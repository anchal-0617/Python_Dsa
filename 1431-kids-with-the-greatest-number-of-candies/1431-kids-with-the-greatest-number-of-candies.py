class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        ans = []
        maximum = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                ans.append(True)
            else:
                ans.append(False)   

        return ans         
        