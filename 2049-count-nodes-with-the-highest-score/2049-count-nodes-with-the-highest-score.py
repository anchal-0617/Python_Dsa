class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        
        n = len(parents)
        children = [[]for _ in range(n)]

        for node in range(1,n):
            children[parents[node]].append(node)

        self.max_score = 0

        self.count = 0
        def solve(node):

        
            size = 1
            score = 1

            for child in children[node]:
                child_size = solve(child)

                size += child_size

                score *= child_size

            remaining = n - size

            if remaining:
                score *= remaining

            if score > self.max_score:
                self.max_score = score

                self.count = 1
            elif score == self.max_score:

                self.count += 1

            return size

        solve(0)

        return self.count                                    