class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for Index, Value in enumerate(nums):
            compensate = target - Value
            if compensate in seen:
                return[seen[compensate], Index]

            seen[Value] = Index