import heapq
from collections import OrderedDict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = OrderedDict()
        for student_id, score in items:
            students[student_id] =  students.get(student_id,[])
            if len(students[student_id]) < 5:
                heapq.heappush(students[student_id],score) 
            else:
                heapq.heappushpop(students[student_id],score)    
        
        result = [[key, int(sum(score)/len(score))] for key, score in students.items()]
        return sorted(result, key = lambda x : x[0])
