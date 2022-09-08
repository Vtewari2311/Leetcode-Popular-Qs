# Approach 1: Brute Force Implementation
# Only consider the range (0, n) even though the range has (0, n + 1) numbers contained in it
# Iterate the input list by creating a hashset and adding all the numbers to it in the given range and finding the missing number through a single pass
# Time Complexity = O(N), Space Complexity = O(N)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        n = len(nums)
        
        for i in range(0, n + 1):
            if i not in hashset:
                return i
       
# Alternate Approach: Sorting 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)):
            if i != nums[i]:
                return(i)
        return(len(nums))
              
# Approach 2: Bit Manipulation
# Conduct an XOR operation on the list of numbers in the range (0, n + 1) and the range (0, n) and it will return the number missing from the latter range
# XOR operation on the list of numbers in range (0, n + 1) take O(N) time and iterate the list of numbers in range (0, n) and XOR with the result which takes O(N) time
# Time Complexity = O(2N), Space Complexity = O(1)

class Solution:
def missingNumber(self, nums: List[int]) -> int:
        xor = 0
		
		//XOR of Indexes
        for i in range(0, len(nums) + 1): xor ^= i
		
		//XOR of Numbers
        for num in nums: xor ^= num
            
		//Finally, xor will be equal to the missing number
        return xor

# Alternate Approach: Sum of List
# Take the sum of the range (0, n + 1) and subtract it from the input range (0, n) then it returns the missing number
# Iterate both lists and find their indviduals sums and then find result
# Time Complexity = O(2N), Space Complexity = O(1)
# This can be done in O(1) time using Gausses formula

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        small_sum = sum(nums)
        big_sum = (n * n + 1 // 2)
        return big_sum - small_sum
      
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      res = len(nums)
      
      for i in range(len(nums) - 1):
        # Subtracting from both the ranges at each index instead of holding two sums
        res += (i - nums[i])
        
      return res
      

