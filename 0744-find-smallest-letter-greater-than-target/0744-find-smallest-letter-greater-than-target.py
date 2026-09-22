class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        low = 0
        high = n-1

        while (low<=high):

            mid = (low+high)//2

            if letters[mid] > target:
                high =mid-1

                

            else:
                low = mid+1

        return letters[low%len(letters)]




        