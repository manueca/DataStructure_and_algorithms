# Function to Reverse words 
def paliendrome_check(Sentence): 
  
    # All in One line 
    return (True if Sentence[::-1]==Sentence[::1] else False )
  
# Driver's Code  
print (paliendrome_check('aba'))
