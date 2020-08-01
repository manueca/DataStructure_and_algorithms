# Function to Reverse Sentence

def reverseSentence(Sentence):
	left=0
	Sentence_lst=Sentence.strip().split(' ')
	right=len(Sentence_lst)-1
	if len(Sentence_lst)==0:
	   return ''
	while left < right:
		print ( Sentence_lst)
		print (left,right)
		Sentence_lst[left],Sentence_lst[right]=Sentence_lst[right],Sentence_lst[left]
		left+=1
		right-=1
	return ' '.join(Sentence_lst)
print (reverseSentence('My Name is Jerry'))
