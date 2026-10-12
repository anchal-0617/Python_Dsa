class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)
        q = deque()
        result  = []

        for i in range (n):

            # maintaining window size
            while q and q[0] <= i-k :
                q.popleft()

            # just kept the larger one
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)
            # jaise hi window k sizee k acc. complete ho jathi hn , append krdenge max element jo ki q[0] pe hnn..
            if i>=k-1:
                result.append(nums[q[0]])

        return result         