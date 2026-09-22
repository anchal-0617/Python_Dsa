class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)

        low = 0
        high = n-1

        while low <= high:

            total = numbers[low] + numbers[high] 


            if total == target:
                return low+1 , high + 1


            elif total < target :

                low+=1

            else:
                high -=1        
