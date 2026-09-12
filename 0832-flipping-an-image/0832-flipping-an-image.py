class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for row in range(len(image)):

            for col in range((len(image) + 1 )//2):

                image[row][col] , image[row][n-col-1] = image[row][n-col-1]^1 , image[row][col]^1

                
              


        return image         


        
        