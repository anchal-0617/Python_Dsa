class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        max_altitude = 0

        for i in range(len(gain)):

            altitude = altitude + gain[i]

            max_altitude = max(max_altitude , altitude)

        return max_altitude    
            
        