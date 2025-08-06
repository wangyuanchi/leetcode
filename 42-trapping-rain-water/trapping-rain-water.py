class Solution:
    def trap(self, height: List[int]) -> int:
        # The amount of water at any index is equal to 
        # min(lMax, rMax) - height[i]
        l, r = 0, len(height) - 1
        lMax, rMax = 0, 0 # Not considering the pointers themselves
        water = 0

        # Calculate amount of water at that pointer before shifting it
        while l <= r:
            if lMax <= rMax: # Calculate water at l pointer
                if height[l] < lMax:
                    water += lMax - height[l]
                lMax = max(lMax, height[l])
                l += 1
            else: # Calculate water at r pointer
                if height[r] < rMax:
                    water += rMax - height[r]
                rMax = max(rMax, height[r])
                r -= 1

        return water