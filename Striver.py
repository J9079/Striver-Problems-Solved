# 838. Linear Search
# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1
# Example 1:
# Input: nums = [2, 3, 4, 5, 3], target = 3
# Output: 1
# Explanation:
# The first occurence of 3 in nums is at index 1

# def targets(nums,target):
#   for i in range(len(nums)):
#     if nums[i] == target:
#       return i
#   return -1
# print(targets([2, 3, 4, 5, 3],6))


# 702. Largest Element
# Given an array of integers nums, return the value of the largest element in the array
# Example 1:
# Input: nums = [3, 3, 6, 1]
# Output: 6
# Explanation: The largest element in array is 6
# Example 2:
# Input: nums = [3, 3, 0, 99, -40]
# Output: 99
# Explanation: The largest element in array is 99


# def largest(nums):
#   i=0
#   j=len(nums)-1
#   while i<j:
#     if nums[i]<nums[j]:
#       i+=1
#     else:
#       j-=1  
#   return nums[i]
# print(largest([3, 3, 0, 99, -40]))



# 695. Second Largest Element
# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
# Example 1:
# Input: nums = [8, 8, 7, 6, 5]
# Output: 7
# Explanation:
# The largest value in nums is 8, the second largest is 7
# Example 2:
# Input: nums = [10, 10, 10, 10, 10]
# Output: -1
# Explanation:
# The only value in nums is 10, so there is no second largest value, thus -1 is returned


# def second(nums):
#   largest=float('-inf')
#   second_largest=float('-inf')
#   for num in nums:
#     if num>largest:
#       second_largest=largest
#       largest=num
#     elif num>second_largest and num!=largest:
#       second_largest=num  
#   if second_largest == float('-inf'):
#     return -1    
#   return second_largest
# print(second([10, 5, 20, 8, 15]))


# 213. Maximum Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1s in the array.
# A binary array is an array that contains only 0s and 1s.
# Example 1:
# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
# Explanation:
# The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

# def maximum(nums ):
#   count=0
#   for i in range(len(nums)-1):
#     if nums[i]==1 and nums[i]==nums[i+1]:
#         count+=1
#   return count
# print(maximum([1, 1, 0, 0, 1, 1, 1, 0]))    

# def maximum(nums ):
#   max_streak=0
#   current_streak=0
#   for num in nums:
#     if num==1:
#       current_streak+=1
#       max_streak=max(max_streak,current_streak)
#     else:
#       current_streak=0  
#   return max_streak
# print(maximum([1, 1, 0, 0, 1, 1, 1, 0]))   


# 832. Left Rotate Array by One
# Given an integer array nums, rotate the array to the left by one.
# Note: There is no need to return anything, just modify the given array.
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]
# Explanation:
# Initially, nums = [1, 2, 3, 4, 5]
# Rotating once to left -> nums = [2, 3, 4, 5, 1]

# def rotate(nums,k):
#   return
# print(rotate([1, 2, 3, 4, 5],1))


# 237. Left Rotate Array by K Places
# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.
# Example 1:
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
# Output: nums = [3, 4, 5, 6, 1, 2]
# Explanation:
# rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]


# 781. Count all Digits of a Number
# You are given an integer n. You need to return the number of digits in the number.
# The number will have no leading zeroes, except when the number is 0 itself.
# Example 1:
# Input: n = 4
# Output: 1
# Explanation: There is only 1 digit in 4.
# Example 2:
# Input: n = 14
# Output: 2
# Explanation: There are 2 digits in 14.

# def count(n):
#   return int(len(str(n)))
# print(count(14))     


# 950. Count number of odd digits in a number
# You are given an integer n. You need to return the number of odd digits present in the number.
# The number will have no leading zeroes, except when the number is 0 itself.
# Example 1:
# Input: n = 5
# Output: 1
# Explanation: 5 is an odd digit.
# Example 2:
# Input: n = 25
# Output: 1
# Explanation: The only odd digit in 25 is 5.

# def odd(n):
#   count=0
#   while n>0:
#     digit=n%10
#     if digit%2!=0:
#       count+=1
#     n//=10  
#   return count
# print(odd(254237))  

# 101. Reverse a number
# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
# Example 1:
# Input: n = 25
# Output: 52
# def reverse(n):
#   rev=0
#   while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
#   return rev
# print(reverse(25))  

# 211. Palindrome Number
# Companies
# You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
# A palindrome number is a number which reads the same both left to right and right to left.
# Example 1:
# Input: n = 121
# Output: true
# Explanation: When read from left to right : 121.
# When read from right to left : 121.

# def palindrome(n):
#   n=str(n)
#   i=0
#   j=len(n)-1
#   is_palindrome=True
#   while  i<j:
#     if n[i]!=n[j]:
#       is_palindrome=False
#       break
#     i+=1
#     j-=1
#   return is_palindrome
# print(palindrome(1231))    

# def palindrome(n):
#   return str(n)==str(n)[::-1]
# print(palindrome(121))    
      
      
# 957. Return the Largest Digit in a Number
# You are given an integer n. Return the largest digit present in the number.
# Example 1:
# Input: n = 25
# Output: 5
# Explanation: The largest digit in 25 is 5      

# def largest(n):
#   n=str(n)
#   i=0
#   j=len(n)-1
#   while i<j:
#     if n[i]<n[j]:
#       i+=1
#     else:
#       j-=1
#   return n[i]
# print(largest(257))   

# 908. Factorial of a given number
# You are given an integer n. Return the value of n! or n factorial.
# Factorial of a number is the product of all positive integers less than or equal to that number.
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: 2! = 1 * 2 = 2.   

# def factoral(n):
#   fac=1
#   for i in range(1,n+1):
#     fac*=i
#   return fac
# print(factoral(5))  


# 937. Check if the Number is Armstrong
# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.
# Example 1:
# Input: n = 153
# Output: true
# Explanation: Number of digits : 3.
# 13 + 53 + 33 = 1 + 125 + 27 = 153.
# Therefore, it is an Armstrong number.

# def armstrong(n):
#   total=0
#   l=len(str(n))
#   temp=n
#   while temp>0:
#     digit=temp%10
#     total+=digit**l
#     temp//=10
#   return n==total  
# print(armstrong(153))  


# 745. Check for Perfect Number
# You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.
# A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.
# Example 1:
# Input: n = 6
# Output: true
# Explanation: Proper divisors of 6 are 1, 2, 3.
# 1 + 2 + 3 = 6.  
# import math
# def perfect(n):
#   if n<=1:
#     return False
#   total=1
#   for i in range(2,int(math.isqrt(n))+1):
#     if n%i==0:
#       total+=i
#       if i*i !=n:
#         total+=n//i   
#   return total==n 
# print(perfect(99999992))

# 779. Check for Prime Number
# You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
# A prime number is a number which has no divisors except 1 and itself.
# Example 1:
# Input: n = 5
# Output: true
# Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

# def primes(n):
  
#   return 
# print(primes(6))


