def permutations(string, step = 0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        print "".join(string)
    for i in range(step, len(string)):
        # copy the string (store as array)
         # swap the current index with the step
        string[step], string[i] =string[i], string[step]
         # recurse on the portion of the stringthat has not been swapped yet
        permutations(string, step + 1)
print (permutations (['o','n','e']))
