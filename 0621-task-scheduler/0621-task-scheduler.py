class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        freq = Counter(tasks)
        

        #     freq = {}

        # for task in tasks:
        #     if task in freq:
        #         freq[task] += 1
        #     else:
        #         freq[task] = 1 


        pq = []

        for value in freq.values():
            heapq.heappush(pq,-value)
        count = 0
        while pq:
            temp = []
            for i in range(n+1):
                if pq:
                    freq = -heapq.heappop(pq)
                    freq -=1
                    temp.append(freq)
            for val in temp:
                if val>0 :
                    heapq.heappush(pq,-val)

            if pq:
                count += n+1
            else:
                count += len(temp)
        return count                                

        