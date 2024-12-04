class Solution: 
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        return [len(set(nums[:i])) - len(set(nums[i:])) for i in range(1, len(nums) + 1)]