class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # solution 1
        for i in range(len(nums)):
            if original in nums:
                original = original * 2
                i+=1
        return original

        # solution 2
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == original:
                original = original * 2
        return original