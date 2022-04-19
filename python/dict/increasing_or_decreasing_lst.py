def decreasing_increasing_lst(lst):
  mid_val=int(round(len(lst)/2))
  min_val=0
  max_val=len(lst)-1
  temp_val=lst[0]
  flg=0
  for i in range(1,len(lst)):
    if lst[i] > temp_val:
      flg+=1
    if lst[i] < temp_val:
      flg-=1
      
  if len(lst)-1==(abs(flg)):
    return True
  else:
    return False

lst=[1,0,-1,-2,-3,4,5]
decreasing_increasing_lst(lst)
