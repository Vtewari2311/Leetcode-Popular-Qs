# Approach 1: Brute Force
# Iterate over the list and compare each element to check for duplicate, requires multiple passes through the list
# Time Complexity: O(N^2), Space Complexity: O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# Approach 2: Sorting
# Sort the intial array if duplicates exist they will be adjacent so only a single pass of the list is needed
# Time Complexity: O(NlogN), Space Complexity: O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]
               return True
        return False

# Approach 3: Hashset
# Insert elements in hashset in O(1) and check values in hashset against values in list to see if a duplicate already exists in the list, requires a single pass
# Memory the hashset requires is equivalent to the size of the input list hence will require extra memory
# Time Complexity: O(N), Space Complexity: O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n is in hashet:
               return True
            hashset.add(n)
        return False
        
# Alternate Approach:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
                return True
        return False
