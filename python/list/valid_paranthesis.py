class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
  
    # Traversing the Expression  
        for char in s: 
            if char in ["(", "{", "["]: 
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                current_char=stack.pop()
                print (current_char,char)
                if char == ')' and current_char!='(':
                    print ('inside')
                    return False
                elif char == '}' and current_char!='{':
                    print ('inside1')
                    return False
                elif char == ']' and current_char!='[': 
                    print ('inside2')
                    return False
        if len(stack)==0:
            return True
        else:
            return False
