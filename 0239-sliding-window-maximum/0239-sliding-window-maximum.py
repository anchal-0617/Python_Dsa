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
            while q and q[0] <= i-k :
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)
            if i>=k-1:
                result.append(nums[q[0]])

        return result         