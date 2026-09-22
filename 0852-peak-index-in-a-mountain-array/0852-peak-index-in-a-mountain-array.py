class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """


        # left = 0
        # right = len(arr)-1

        # while(left<=right):

        #     mid = (left+right)//2

        #     if mid <
        
        max_element = arr[0]

        max_index = 0
        for i in range(len(arr)):

            if arr[i] > max_element:
                max_element = arr[i]
                max_index = i

        return max_index
