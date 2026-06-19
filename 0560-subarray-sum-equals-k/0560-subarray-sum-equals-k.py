class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

        prefix_sum = 0
        count =  0

        hashm = {0:1}

        for i in nums:

            prefix_sum += i

            req = prefix_sum - k

            if req in hashm:
                count += hashm[req]

            hashm[prefix_sum] = hashm.get(prefix_sum,0)+1
        return count    
