def find_anagrams(sent:string):
	sent='Listen to Silent People'
	dict_anagrams={}
	sent_lst=sent.split()
	for i in range(len(sent_lst)):
		sent_lst[i]
		sent_temp=list(sent_lst[i].upper())
		sent_sort=''.join(sorted(sent_temp))
		print ('sorted temp is ',sent_temp)
		print ('sorted is ',sent_sort)
		print (sent_sort)
		if dict_anagrams.get(hash(sent_sort),1000000)==1000000:
			dict_anagrams[hash(sent_sort)]=[sent_lst[i]]
		else:
			print ('dict values are ',dict_anagrams[hash(sent_sort)])
			type(dict_anagrams[hash(sent_sort)])
			inter=dict_anagrams[hash(sent_sort)]
			inter.append(sent_lst[i])
			print('inter value is ',inter)
			dict_anagrams[hash(sent_sort)]=inter
			print ('dict values are ',dict_anagrams[hash(sent_sort)])

	values =[v for v in dict_anagrams.values()]
	anagram_val=[]
	for i in values:
		if len(i) >1 :
			anagram_val=i

	return anagram_val
