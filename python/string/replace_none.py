"""
Replace none value in a list
"""

def replace_none(a):
	prev=''
	for i in range(len(a)):
		if a[i] == 'None':
			a[i]=prev
		prev=a[i]
				
	return a

a=['My','Name', 'None', 'Jerry']
print (replace_none(a))
