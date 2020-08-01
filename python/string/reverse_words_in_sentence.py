# Function to Reverse words 
def reverseWordSentence(Sentence): 
  
    # All in One line 
    return ' '.join(word[::-1] for word in Sentence.split(" ")) 
  
# Driver's Code  
print (reverseWordSentence('My Name is Jerry'))

