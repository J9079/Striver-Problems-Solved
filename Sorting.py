# def partition(arr,first,last):
#   if first>=last : return
#   pivotindex= findpivot(arr,first,last)
#   partition(arr,first,pivotindex-1)
#   partition(arr,pivotindex+1,last)   

# def findpivot(arr,first,last):
#   pivot=arr[last]
#   i=first-1
#   for j in range(first,last):
#     if arr[j]<pivot:
#       i+=1
#       swap(arr,i,j)
#   i+=1
#   swap(arr,i,last)
#   return i    
# def swap(arr,i,j):
#   temp=arr[i]
#   arr[i]=arr[j]
#   arr[j]=temp
# arr=[18,5,3,40,10,30]
# partition(arr,0,len(arr)-1)     
# print(arr)   
   
   
# def cyclic(arr):
#   for i in range(len(arr)):
#     correct_index=arr[i]-1
#     if arr[i]!=arr[correct_index]:
#       temp=arr[i]
#       arr[i]=arr[correct_index]
#       arr[correct_index]=temp

#   return arr    
# print(cyclic([7,6,3,8,5,1,2,4]))      

# def cyclic(arr):
#   i=0
#   while i<len(arr):
#     correct_index=arr[i]-1
#     if arr[i]!=arr[correct_index]:
#       temp=arr[i]
#       arr[i]=arr[correct_index]
#       arr[correct_index]=temp
#     else:
#       i+=1  
#   return arr    
# print(cyclic([7,6,3,8,5,1,2,4]))   


# Question 1 :
# You are given an array of non-negative integers where each element represents the height of a building in a 1D landscape. The width of each building is 1 unit. Your goal is to determine how much rainwater can be trapped between the buildings after it rains. The trapped water is represented by the empty space between the taller buildings. 

# Example 1
# Sample Input
# 1
# [0,2,1,0,3,1,0,1,2,1,2,1]
# Sample Output
# 8

# def trapping(arr):
#   trap=0
#   left_max=0
#   right_max=0
#   left=0
#   right=len(arr)-1
#   while left<right:
#     if arr[left]<arr[right]:
#       left_max=max(left_max,arr[left])
#       trap+=left_max-arr[left]
#       left+=1
#     else:
#       right_max=max(right_max,arr[right])
#       trap+=right_max-arr[right]
#       right-=1
#   return trap
# print(trapping([0,2,1,0,3,1,0,1,2,1,2,1]))      

# Question 2 :
# You are given an array arr with n elements, where each element represents an object colored either red, white, or blue.
# Your task is to sort the array in-place so that objects of the same color are grouped together, with the order being red first, followed by white, and then blue.
# You must implement the solution without using any built-in sort functions. 
# Example 1
# Sample Input
# 1
# [2,1,2,0,1,0]
# Sample Output
# [0, 0, 1, 1, 2, 2]
     
    
# def arrangment(arr):
#   i=0
#   k=len(arr)-1
#   j=0
#   while i<=k:
#     if arr[i]==0:
#       temp=arr[i]
#       arr[i]=arr[j]
#       arr[j]=temp
#       j+=1
#       i+=1
#     elif arr[i]==2:
#       temp=arr[i]
#       arr[i]=arr[k]
#       arr[k]=temp
#       k-=1
#     else:
#       i+=1
#   return arr      
# print(arrangment([2,1,2,0,1,0])) 





# Question 3 :
# Given a sorted array of integers, remove the duplicate elements in-place such that each unique element appears only once.
# Return the count of unique elements.
# Note:
# 	•	Do not use any additional space.
# 	•	The relative order of elements should be maintained.
# 	•	Only the first part of the array should be updated with unique elements. 
# Example 1
# Sample Input
# 1
# [1, 1, 2]
# Sample Output

# def uniqu(nums):
#   if not nums:
#     return 0
#   i=0
#   for j in range(1,len(nums)):
#     if nums[j] !=nums[i-1]:
#       i+=1
#   return i
# print(uniqu([1,1,2]))



# Question 4 :
# Given an array of 0's and 1's, move all the zeros to the end of the array. You can use extra space to perform this operation. 
# Example 1
# Sample Input
# 5
# 0 1 0 1 1
# Sample Output
# 1 1 1 0 0

# def moves(nums):
#   first=0
#   for last in range(len(nums)):
#     if nums[last] !=0:
#       nums[first],nums[last]=nums[last],nums[first]
#       first+=1
#   return nums
# print(moves([0,1,0,1,1]))    

# Question 5 :
# You are given two sorted integer arrays arr1 and arr2 in non-decreasing order, along with two integers m and n, representing the number of elements in arr1 and arr2 respectively.
# You need to merge arr2 into arr1 to form a single sorted array.
# Note that arr1 has enough space to hold the additional elements from arr2 (its total size is m + n, where the first m elements contain valid data and the remaining positions are filled with 0s). You should ignore these 0s and overwrite them with the elements from arr2. arr2 contains exactly n elements.
# The final merged array should be stored within arr1. 
# Example 1
# Sample Input
# 1
# 2 2
# [1, 5, 0, 0]
# [2, 3]
# Sample Output

# [1, 2, 3, 5]


# def sequence(arr1,arr2,m,n):
#   i=m
#   j=n
#   k=len(arr1)-1
#   while i<k:
#     if arr1[i]>arr2[j]:
#       arr1[k]=arr1[i]
#       k-=1
#       i-=1
#     else:
#       arr1[k]=arr2[j]
#       k-=1
#       j-=1   
#   return arr1
# print(sequence([1, 5, 0, 0],[2,3],1,1))

# def sequence(arr1, arr2, m, n):
#   p1 = m - 1  
#   p2 = n - 1  
#   p_merged = m + n - 1 
#   while p1 >= 0 and p2 >= 0:
#     if arr1[p1] > arr2[p2]:
#       arr1[p_merged] = arr1[p1]
#       p1 -= 1
#     else:
#       arr1[p_merged] = arr2[p2]
#       p2 -= 1
#     p_merged -= 1

#   while p2 >= 0:
#     arr1[p_merged] = arr2[p2]
#     p2 -= 1
#     p_merged -= 1
#   return arr1
# print(sequence([1, 5, 0, 0],[2,3],2,2))

# def sequence(arr1,arr2):
#   m=len(arr1)-1
#   n=len(arr2)-1
#   i=0
#   j=0
#   k=0
#   while i<m and j<n:
#     if arr1[i]< arr2[j]:
#       arr1[k]=arr1[i]
#       k+=1
#       i+=1
#     else:
#       arr1[k]=arr2[j]  
#       k+=1
#       j+=1
#     i+=1
#     j+=1  
#   return arr1
# print(sequence([1, 5, 0, 0],[2,3]))