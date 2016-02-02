

def oddTuples(aTup):

    max = len(aTup)

    newTup = ()
    i = 0
    while i < max:
        newTup += (aTup[i],)
        i += 2
    return(newTup)

print(oddTuples((1, 8, 7, 15, 3, 5, 14, 1)))

