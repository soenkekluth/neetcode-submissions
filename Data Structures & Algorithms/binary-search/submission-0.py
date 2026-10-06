class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = (low + high) // 2
            current = nums[mid]
            if current == target:
                return mid
            if target < current:
                high = mid -1
            else:
                low = mid + 1
        
        return -1

sol = Solution()
print(sol.search([-1,0,2,4,6,8], 4))
