class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        q=str(abs(numerator)//abs(denominator))
        reminder=float(abs(numerator)%abs(denominator))
        hs_mp={}
        ans=[]
        sign =1
        if numerator==0:
            return '0'
        if numerator<0 and denominator<0:
            sign=1
        elif numerator<0 or denominator<0:
            sign=-1
        
        denominator=abs(denominator)
        numerator=abs(numerator)


        print ('sign is ',sign)
        ans.append(q)
        if reminder ==0:
            
            return str(int(''.join(ans)) * sign)
        
        if reminder >0 :
            ans.append('.')

            hs_mp={}
            while reminder >0 :
                
                if hs_mp.get(reminder,0)!=0:
                    pos=hs_mp[reminder]
                    ans.insert(pos,'(')
                    ans.append(')')
                    break
                else:
                    hs_mp[reminder]=len(ans)
                    reminder *=10
                    quotient=str(int(reminder)//int(denominator))
                    ans.append(str(quotient))
                    reminder = reminder % denominator


                    
                print ('ans is ',ans)
                #hs_mp[reminder]=int(hs_mp.get(reminder,0))+1
                #if hs_mp[reminder] >1:
                #    ans+='('
                
            if sign == -1:
                ans.insert(0,'-')
            
            return ''.join(ans)