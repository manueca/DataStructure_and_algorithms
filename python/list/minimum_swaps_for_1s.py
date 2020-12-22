class Solution:
    def minSwaps(self, data: List[int]) -> int:
        cnt=0
        cnt_zero=0
        for i in data:
            if i==1:
                cnt+=1
        print(cnt)
        if cnt ==0 or cnt ==1:
            return 0
        max_val=cnt
        min_val=0
        min_swap=10000000
        for i in range(min_val,max_val):
                if data[i] == 0:
                    cnt_zero+=1
        while max_val< len(data)-1:
            min_swap=min(min_swap,cnt_zero)
            min_val+=1
            max_val+=1
            if data[min_val-1]==0:
                cnt_zero-=1
            if data[max_val]==0:
                cnt_zero+=1
                
                
                
        return min_swap