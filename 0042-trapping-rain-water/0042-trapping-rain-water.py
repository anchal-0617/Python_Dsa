class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        stack = []

        water = 0
        # we use stack here , dont forgot r=the logic , seedha sa funda h jab badi height aagyi mtlb water loging hogi whi condn lagayegi hn and use right kahege , left humne store kr hi lia h bottom nikl hi lia h once this done hum biunded_height k formula m put kardenge and we get that alright !
        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:

                bottom = stack.pop()

                if not stack:
                    break

                left = stack[-1]

                width = i - left -1

                bounded_height = min(height[left] , height[i]) - height[bottom]


                water += width * bounded_height
            stack.append(i)    


        return water            
        