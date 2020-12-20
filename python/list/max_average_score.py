
"""
Given a file containing data of student name and marks scored by him/her in 3 subjects. The task is to find the list of students having the maximum average score.
Note : If more than one student has the maximum average score, print them as per the order in the file.

Examples:

Input : file[] = {“Shrikanth”, “20”, “30”, “10”, “Ram”, “100”, “50”, “10”}
Output : Ram 53
Average scores of Shrikanth, Ram are 20 and 53 respectively. So Ram has the maximum average score of 53.

Input : file[] = {“Ramesh”, “90”, “70”, “40”, “Adam”, “50”, “10”,
            ”40″, “Suresh”, “22”, “1”, “56”, “Rocky”, “100”, “90”, “10”}
Output : Ramesh Rocky 66
Average scores of Ramesh, Adam, Suresh and Rocky are 66, 33, 26 and 66 respectively. So both Ramesh and Rocky have the maximum average score of 66.
"""


def getStudentsList(file):
	dict_val={}
	max_val=0
	if len(file)==0:
		return 0
	for i in range(0,len(file)):
		if i==0 or i%4==0:
			sumVal=0
			cnt=0
			avg=0
			dict_val[file[i]]=0
			name=file[i]
		else:	
			cnt+=1
			sumVal+=int(file[i])
			ret_val=(sumVal)/cnt
			dict_val[name]=ret_val
			print ("max_val is ,",max_val,ret_val)
	for k,v in dict_val.items():
		if max(max_val,v)==v:
			nax_val=v
			ret=k
	print (ret)
	return ret

file = ["Shrikanth", "20", "30", "10",  
    "Ram", "100", "50", "10"]  
getStudentsList(file)  