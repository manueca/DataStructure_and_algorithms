class solution:
	def studentWithHighestAverage(self,input:list) -> str:
		student_score={}
		print('input is ',inp)
		for i in inp:
			val=i.pop()
			key=i.pop()
			score=student_score.get(key,[])
			score.append(val)
			student_score[key]=score
		max_average=0
		for k,v in student_score.items():
			sum=0
			count=0
			average=0
			for j in v:
				sum+=int(j)
				count+=1
			average=(sum/count)
			max_average=max(max_average,average)
			if max_average==average:
				result=k
		return result



inp=[{"Bob","87"}, {"Mike", "35"},{"Bob", "52"}, {"Jason","35"}, {"Mike", "55"}, {"Jessica", "99"}]
inst=solution()
print(inst.studentWithHighestAverage(inp))