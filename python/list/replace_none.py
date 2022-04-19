def replace_none(lst):
  temp_val=lst[0]
  for i in range(1,len(lst)-1):
    if lst[i] is None:
      lst[i]=temp_val
    else:
      temp_val=lst[i]
  return lst
      
    

lst=[1,4,None,None,3]
replace_none(lst)
