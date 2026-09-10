class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = list(set(nums))
        nums.sort()
        ans = []
    
        i = 1
        for j in range(len(nums)):

            while i < nums[j]:
                ans.append(i)
                i+=1


            if nums[j] == i:
                i+=1
                
            
        while i <=n:
            ans.append(i)  
            i+=1
              

        return ans          