# 852. Peak Index in a Mountain Array
# premium lock icon
# Companies
# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
# Return the index of the peak element.
# Your task is to solve it in O(log(n)) time complexity.
# Example 1:
# Input: arr = [0,1,0]
# Output: 1
# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# def peak(arr):
#   f=0
#   l=len(arr)-1
#   while f<l:
#     mid=(f+l)//2
#     if arr[mid]<=arr[mid+1]:
#       f=mid+1
#     else:
#       l=mid
#   return f 
# print(peak([24,69,100,99,79,78,67,36,26,19]))

# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# def targets(nums,target):
#   f=0
#   l=len(nums)-1
#   while f<=l:
#     mid=(f+l)//2
#     if nums[mid]==target:return mid
#     if nums[f]<=nums[mid]:
#       if nums[f]<=target and target<=nums[mid]:
#         l=mid
#       else:
#         f=mid+1
#     else:
#       if nums[mid+1]<=target and target<=nums[l]:
#         f=mid+1
#       else:
#         l=mid 
#   return -1      
# print(targets([1],1))      
              
# 103. Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:
# Input: root = [1]
# Output: [[1]]
# Example 3:
# Input: root = []
# Output: []          


# Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

# Each student receives atleast one book.
# Each student is assigned a contiguous sequence of books.
# No book is assigned to more than one student.
# All books must be allocated.
# The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum. If it is not possible to allocate books to all students, return -1;

# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Allocation can be done in following ways:
# => [12] and [34, 67, 90] Maximum Pages = 191
# => [12, 34] and [67, 90] Maximum Pages = 157
# => [12, 34, 67] and [90] Maximum Pages = 113.
# The third combination has the minimum pages assigned to a student which is 113.
# Input: arr[] = [15, 17, 20], k = 5
# Output: -1
# Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

def pages(arr):
  first=0
  last=0
  ans=-1
  for i in range(len(arr)):
    last+=arr[i]
    first=max(arr[i],first)
  while first<=last:
    mid=(first+last)//2
    if   