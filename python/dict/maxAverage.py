import collections


def findMaxAvg(s: list)
  d = collections.defaultdict(list)
   for k, v in s:
        d[k].append(v)
    sum_val = 0
    cnt = 0
    max_avg = 0
    for i in d.items():
        print(i[0])
        print(i[1])
        for j in range(len(i[1])):
            sum_val = +i[1][j]
            cnt += 1
        max_avg = max(max_avg, sum_val/cnt)

    return (max_avg)
