class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=0 
        water_trapped=0
        right_max=len(height)-1
        leftWall,rightWall=0,0
        while left_max < right_max :
            if height[left_max] < height[right_max]:
                if height[left_max]> leftWall :leftWall=height[left_max]
                else: water_trapped+=leftWall-height[left_max]
                left_max+=1
            else:
                if height[right_max]> rightWall :rightWall=height[right_max]
                else: water_trapped+=rightWall-height[right_max]
                right_max-=1

        return water_trapped
