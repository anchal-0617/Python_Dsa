class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        low = max(nums)

        high = sum(nums)

        while ( low<high):

            mid = (low+high)//2

            subarray = 1

            weight = 0

            for num in nums:

                if weight + num > mid:
                    subarray +=1
                    weight = 0

                weight += num

            if subarray <= k:

                high = mid

            else:

                low = mid+1

        return low            

