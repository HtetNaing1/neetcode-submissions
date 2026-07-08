class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            last = nums[i]
            cur = nums[i + 1]
            if cur == last:
                return True
            i+=1
        return False


