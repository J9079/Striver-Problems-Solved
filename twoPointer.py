# Question 1 :
# Link - https://leetcode.com/problems/valid-palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false

# def palindrome(s):
#   is_palindrome=True
#   i=0
#   j=len(s)-1
#   while i<j:
#     if not s[i].isalnum():
#       i+=1
#       continue
#     if not s[j].isalnum():
#       j-=1
#       continue
#     if s[i].lower() !=s[j].lower():
#       i+=1
#       j-=1
#       is_palindrome=False
#       break
#     i+=1
#     j-=1
#   return is_palindrome
# print(palindrome("A man, a plan, a canal: Panama"))    
      



# Question 2 :
# link - https://leetcode.com/problems/is-subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# def subsequence(s,t):
#   if len(s)!=len(t):
#     return False
#   is_sequence=True
#   for i in range(len(s)):
#     for j in range(len(t)):
#       if s[i] not in t[j]:
#         is_sequence=False
#   return is_sequence
# print(subsequence("abc","ahbgdc"))

# def subsequence(s,t):
#   i=0
#   j=0
#   while i<len(s) and j<len(t):
#     if s[i]==t[j]:
#       i+=1
#     j+=1  
#   return i==len(s) 
# print(subsequence("axc","ahbgdc"))



# Question 3 :
# link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# def same(numbers,target):
#   dec={}
#   for i in range(len(numbers)):
#     valid=target-numbers[i]
#     if valid in numbers:
#       return [dec[numbers],i]
#     dec[numbers]=i  
#   return
# print(same([2,7,11,15],9))

# def same(numbers,target):
#   for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#       if numbers[i]+numbers[j]==target:
#         return [i,j]
# print(same([-1,0],-1))


# def same(numbers,target):
#   dec={}
#   for index, num in enumerate(numbers):
#     valid=target-num
#     if valid in dec:
#       return [dec[valid],index+1]
#     dec[num]=index+1
#   return dec
# print(same([-1,0],-1))


# def Sum(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#     while left < right:
#         current_sum = numbers[left] + numbers[right]
#         if current_sum == target:
#             return [left + 1, right + 1]
#         elif current_sum < target:
#             left += 1
#         else: 
#             right -= 1
#     return []
# print(Sum([-1,0],-1))  

# Question 1 :
# link - https://leetcode.com/problems/container-with-most-water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Example - 1
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# def maxWater(height):
#   ans=0
#   left=0
#   right=len(height)-1
#   while left<right:
#     ans =max(ans,(min(height[left],height[right])*(right-left)))
#     if height[left]<height[right]:
#       left+=1
#     else:  
#       right-=1  
#   return ans
# print(maxWater([1,8,6,2,5,4,8,3,7]))


# Question 2 :
# link - https://leetcode.com/problems/3sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


# def ThreeSum(nums):
#   nums.sort()
#   ans=[]
#   for i in range(len(nums)-2):
#     if i!=0 and nums[i-1]==nums[i]:
#       continue
#     j=i+1
#     k=len(nums)-1
#     while j<k:
#       sum=nums[i]+nums[j]+nums[k]
#       if sum==0:
#         ans.append([nums[i],nums[j],nums[k]])
#         while j<k and nums[j+1]==nums[j]:
#           j+=1
#         while j<k and nums[k-1]==nums[k]:
#           k-=1
#         j+=1
#         k-=1
#       elif sum<0:
#         j+=1
#       else:
#         k-=1
        
#   return ans
# print(ThreeSum([-1,0,1,2,-1,-4]))
            

   
   