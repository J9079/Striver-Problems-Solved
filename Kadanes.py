# def subarray(nums):
#   max_sum=0
#   for i in range(len(nums)):
#     current_sum=0
#     for j in range(i,len(nums)):
#       current_sum+=nums[j]
#       max_sum=max(max_sum,current_sum)
#   return max_sum    
# print(subarray([3,-4,-5,4,-1,7,8]))     

# def kadane(nums):
#   values=[]
#   max_sum=nums[0]
#   current_sum=nums[0]
#   for i in range(1,len(nums)):
#     current_sum=max(nums[i],current_sum+nums[i])
#     max_sum=max(current_sum,max_sum)
#     if current_sum<0: 
#       current_sum=0
      
#     values.append(max_sum)  
#   return max_sum ,values
# print(kadane([5,-3,5])) 


# def kadane(nums):
#   max_sum=float('-inf')
#   current_sum=0
#   for num in nums:
#     current_sum+=num
#     if current_sum>max_sum:
#       max_sum=current_sum
#     if current_sum<0:
#       current_sum=0  
#   return max_sum 
# print(kadane([-1]))      


def maximum_sum(nums):
  total=sum(nums)
  current_max=nums[0]
  max_sum=nums[0]
  
  current_min=nums[0]
  min_sum=nums[0]
  n=len(nums)
  for i in range(1,n):
    current_max=max(nums[i],current_max+nums[i])
    max_sum=max(max_sum,current_max)
    
    current_min=min(nums[i],current_min+nums[i])
    min_sum=min(min_sum,current_min)
  if max_sum<0:  
      return max_sum
  sum_values=total-min_sum
  return max(max_sum,sum_values)
print(maximum_sum([5,-3,5]))

# def merge_sort(nums):
#   if len(nums)<=1:
#     return nums
#   mid=len(nums)//2
  
#   left=nums[:mid]
#   right=nums[mid:]
#   left=merge_sort(left)
#   right=merge_sort(right)
  
#   return merge(left,right)
# def merge(left,right):
#   result=[]
#   i=0
#   j=0
#   while i<len(left) and j<len(right):
#     if left[i]<right[j]:
#       result.append(left[i])
#       i+=1
#     else:
#       result.append(right[j])
#       j+=1
#   while i<len(left):
#     result.append(left[i])
#     i+=1
#   while j<len(right):
#     result.append(right[j])
#     j+=1   
#     result      
#   return result
# nums=[38, 27, 43, 3, 9, 82, 10]
# print(merge_sort(nums))



# def merge_sort(nums):
#   result=[]
#   i=f=0
#   mid=len(nums)//2
#   j=mid+1 
#   l=len(nums)-1
#   k=0
#   while i<mid and j<=l:
#     if nums[i]<nums[j]:
#        result.append(nums[i])
#        i+=1
#     else:
#       result.append(nums[j])
#       j+=1
#   while i<=mid:
#       result.append(nums[i])
#       i+=1
#   while j<=l:
#     result.append(nums[j])
#     j+=1      
#   while k<len(result) :
#     nums[i]=result[k]
#     k+=1
#     i+=1        
#   return result
# print(merge_sort([38, 27, 43, 3, 9, 82, 10]))