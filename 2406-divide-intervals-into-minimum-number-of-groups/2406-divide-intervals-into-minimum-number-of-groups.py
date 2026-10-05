class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()

        heap = []
        for start , end in intervals:

            if heap and heap[0]<start:

                heapq.heappop(heap)

            heapq.heappush(heap,end)  

        return len(heap)    

        