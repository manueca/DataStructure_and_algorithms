
# Brute force approach .
# Complexity if O(N^2) 
def findSubstring(s):
	max_val=0
	for i in s:
		append_val=[]
		pal_val={}
		temp_str=''
		for j in s:
			append_val.append(j)
			if append_val==append_val[::-1]:
				print (append_val)
				max_val=max(len(append_val),max_val)
				if max_val==len(append_val):
					pal_val[max_val]=temp_str.join(append_val)
		return pal_val[max(k for k in pal_val)]



