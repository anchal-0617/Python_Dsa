class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """


        ans = [0] * 101

        for borth , death in logs:
            ans[borth - 1950] += 1
            ans[death - 1950] -=1

        max = ans[0]
        result = 0

        for i in range(1,101):
            ans[i] += ans[i-1]

            if ans[i] > max:
                max = ans[i]

                result = i
        return result + 1950        