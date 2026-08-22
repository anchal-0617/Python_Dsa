class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key = lambda x : x[0])
        result = []

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if not result or result[-1][1] < start:
                result.append([start , end])

            else:
                result[-1][1] = max(result[-1][1] , end)

        return result            


        