def findNthHighest(dict_val,n):
        nth_max_value=sorted(set(dict_val.values()),reverse=True)[-n]
        return nth_max_value

dict_val = {"a":1,"b":5,"c":3,"d":3}
print (findNthHighest(dict_val,2))

