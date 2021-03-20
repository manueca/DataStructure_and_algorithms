"""
Given two sentences, you have to print the words those are not present in either of the sentences.(If one word is present twice in 1st sentence but not present in 2nd sentence then you have to print that word too)
"""

def missing_word(a,b):
	a_dict={}
	b_dict={}
	result=[]
	for i in a.split():
		a_dict[i] = a_dict.get(i, 0) + 1
	for i in b.split():
                b_dict[i] = b_dict.get(i, 0) + 1
	for i,j in a_dict.items():
		if b_dict.get(i,0) !=j:
			result.append(i)
	for i,j in b_dict.items():
		if a_dict.get(i,0) !=j and i not in result:
			result.append(i)
	return result

a='My Name is Jerry'
b='My Name is Jittu'
print (missing_word(a,b))
