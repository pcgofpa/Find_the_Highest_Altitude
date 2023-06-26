class Solution:
    def largest_Altitude(gain):
        n = len(gain)
        heighest_point = 0
        height_change = 0
        
        for i in range(n):
            height_change += gain[i]
            heighest_point = max(heighest_point, height_change)
            
        return heighest_point        
        
        
    print(f"Trip 1: heighest point is {largest_Altitude([-5,1,5,0,-7])}")
    print(f"Trip 2: heighest point is {largest_Altitude([-4,-3,-2,-1,4,3,2])}")