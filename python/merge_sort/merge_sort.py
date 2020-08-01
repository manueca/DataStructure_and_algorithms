"""
Step 1- split
Given a list let’s split it into two lists right down the middle
"""
def split(lst):
	median=len(lst)//2
	return lst[0:median],lst[median:len(lst)]
"""
Step 2- merge sorted lists
Given two sorted lists we should be able to “merge” them into a single list in a linear operation.
"""
def merge_sorted_lists(left_lst,right_lst):
	i=0
	j=0
	if len(left_lst)==0:
	   return right_lst
	if len(right_lst)==0:
	   return left_lst
	merged_lst=[]
	full_length=len(left_lst)+len(right_lst)
	while len(merged_lst)<full_length:
		print (left_lst[i],right_lst[j])
		if left_lst[i] <=  right_lst[j] :
		   merged_lst.append(left_lst[i])
		   print ("left value is ",left_lst[i])
		   i+=1
		else:
		   print ("Right value is ",right_lst[j])
		   merged_lst.append(right_lst[j])
		   j+=1
		if i > len(left_lst)-1:
		   merged_lst+=right_lst[j:]
		   break
		if j > len(right_lst)-1:
		   merged_lst+=left_lst[i:]
		   break
	return merged_lst

"""
Step 3- merge sort
Merge sort only needs to utilize the previous 2 functions
We need to split the lists until they have a single element
A list with a single element is sorted
Now we can merge these single-element (or empty) lists

"""
def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        # The following line is the most important piece in this whole thing
        return merge_sorted_lists(merge_sort(left), merge_sort(right))

print(merge_sort([1,4,23,4242,112,]))
