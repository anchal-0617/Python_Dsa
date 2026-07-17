class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """


        stack = []

        for a in asteroids:

            while stack and a<0 and stack[-1] >0 :
                sum = a + stack[-1]

                if sum < 0:
                    stack.pop()

                elif sum > 0:

                    break

                else :
                    stack.pop()
                    break
            else :

                stack.append(a)

        return stack                        
        