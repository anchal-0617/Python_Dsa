class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """


        stack = []

        for a in asteroids:
            #jab tk stack m hn tab tk check krege bcz collision mai sabko check krna hn + rightly understand the 3 condns and for undeerstaning purpose , use test case[10,2,-5,8,-8] , Collision with 2: -5 + 2 = -3. Since the sum is negative, 2 is destroyed. Next, -5 collides with 10: -5 + 10 = 5. The sum is positive, so break destroys -5.

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
        