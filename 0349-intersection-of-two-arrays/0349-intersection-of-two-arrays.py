class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        ans = []
        for i in range(len(nums1)):
            
            for j in range(len(nums2)):
                

                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])

            

        return ans            
        