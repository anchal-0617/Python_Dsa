class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # intervals.sort()
        # count = 0
        # for i in range(len(intervals)-1):

        #     start = intervals[i][0]
        #     end = intervals[i][1]

        #     if end == intervals[i+1][0] or (end > intervals[i+1][0] and intervals[i+1][1] <= start ):

        #         continue

        #     else:
        #         count +=1    
        # return count
        

        intervals.sort(key = lambda x:x[1])

        count = 0
        end = intervals[0][1]

        for i in range(1 , len(intervals)):
            start = intervals[i][0]

            if start < end:

                count +=1

            else:

                end = intervals[i][1]    

        return count        

