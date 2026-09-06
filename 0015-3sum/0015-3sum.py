class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        

        

        
        nums.sort()
        n = len(nums)
        result = set()
        for i in range(n-2):

            left = i+1
            right = n-1

            while left < right :
                
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:

                    

                    result.add((nums[i] , nums[left] , nums[right]))
                    left += 1
                    right -=1
                    

                elif summ < 0:
                    left += 1

                else:
                    right -= 1

                  

        return [list(x) for x in result]          





                     
        