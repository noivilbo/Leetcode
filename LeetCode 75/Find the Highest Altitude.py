class Solution(object):
    def largestAltitude(self, gain):
        max_altitude = 0
        current_altitude = 0
        for i in gain:
            current_altitude +=i
            max_altitude = max(max_altitude,current_altitude)
        return max_altitude
