"""
Check if a list contents are increasing or decreasing
"""

def monotonic_check(a):
	monotnic=''
	prev=''
	for i in range(1,len(a)):
		if a[i] > a[i-1] :
			monotnic='I'
		elif a[i] < a[i-1]:
			monotnic='D'
		else:
			return 'False'
		if monotnic == prev or  i==1:
			prev=monotnic
		else:
			return 'False'
				
	return 'True'

a=[10,8,7,6,5]

print (monotonic_check(a))
