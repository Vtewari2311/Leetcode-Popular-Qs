# Approach 1: Brute Force
# Time Complexity O(N), Space Complexity O(N)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        List = set(range(1, len(nums) + 1))
        nums = set(nums)
        return list(List.difference(nums))
      
# Approach 2: Enumeration
# Time Complexity O(N), Space Complexity O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing
        for n in nums:
          i = abs(n) - 1
          nums[i] = - 1 * abs(nums[i])
          
        res = []
        for i, n in enumerate(nums):
          if n > 0:
            res.append(i + 1)
        return res

