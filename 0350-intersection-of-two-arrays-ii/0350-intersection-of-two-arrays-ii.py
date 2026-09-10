class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = {}
        ans = []
        
        for i in range(len(nums1)):
            freq[nums1[i]] = freq.get(nums1[i],0)+1


            
        for j in range(len(nums2)):
            if nums2[j] in freq and freq[nums2[j]] >0:

                

                
                    
                ans.append(nums2[j])
                freq[nums2[j]] -= 1

            

        return ans    
        