class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """


        ans = []
        n = len(intervals)
        freq = {}
        
        for i in range(len(intervals)):
            
            start = intervals[i][0]

            ans.append(start)

            freq[start] = i

        ans.sort() 
        index = []  

        

        for i in range(len(intervals)):
            result = -1
            low = 0
            high = n-1
            end = intervals[i][1]

            while(low<=high):

                mid = (low+high)//2

                if ans[mid]>=end:
                    result = freq[ans[mid]]
                    high = mid-1

                else:
                    low = mid+1

            index.append(result)

        return index                





        