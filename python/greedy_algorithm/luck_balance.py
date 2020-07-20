#!/bin/python3
"""
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers,  and :

 is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by ; if she loses it, her luck balance will increase by .
 denotes the contest's importance rating. It's equal to  if the contest is important, and it's equal to  if it's unimportant.
If Lena loses no more than  important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.

For example,  and:

Contest		L[i]	T[i]
1		5	1
2		1	1
3		4	0
If Lena loses all of the contests, her will be . Since she is allowed to lose  important contests, and there are only  important contests. She can lose all three contests to maximize her luck at . If , she has to win at least  of the  important contests. She would choose to win the lowest value important contest worth . Her final luck will be .

"""
import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    n=len(contests)
    print (contests)
    for i in range(0,n-1):
        for j in range(n - i - 1):
            if contests[j]<contests[j+1]:
                contests[j],contests[j+1]=contests[j+1],contests[j]
    print (contests)
    sum=0
    min=0
    for i,j in contests:
        if j==1 and k!=0:
            print ("most important sums:",i,j,k,sum)
            sum=sum+i
            k-=1
        elif j==1:
            print ("most important substracts:",i,j,k,sum)
            sum=sum-i
        else:
            print ("least important sums:",i,j,k,sum)
            sum=sum+i
    return sum
