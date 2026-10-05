class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = dict()
        for i in range(len(nums)):
            if nums[i] not in x:
                x[nums[i]] = 0
            elif nums[i] in x:
                return True
        return False