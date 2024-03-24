class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def dfs(low, high):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] < target:
                return dfs(mid +1, high)
            elif nums[mid] > target:
                return dfs(low, mid-1)
            else:
                return mid
        return dfs(0, len(nums)-1)
