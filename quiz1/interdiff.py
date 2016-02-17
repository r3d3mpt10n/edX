def dict_interdiff(d1, d2):

    ## This part is now correct.
    intersect = {}
    for key in d2.keys():
        if key not in (d1):
            intersect[key] = d2[key]
    for key in d1.keys():
	if key not in (d2):
	    intersect[key] = d1[key]
   
    diff = {}

    for key in d2.keys():
        if (key in (d1)):
	    if d1 == d2:
		diff[key] = d1[key] + d2[key] 
	    elif len(d1) > len(d2):
		 diff[key] = d1[key] + d2[key]
            	#diff[key] = (d2[key])
            if (d2[key] != d1[key]):
            	diff[key] = (d1[key] < d2[key])
	    elif d1[key] == d2[key]:
		diff[key] = (d2[key] > d1[key])


    #for key in d2.keys():
        #if (not key in (d1)):
            	#diff[key] = (d2[key])

   
    return (diff,intersect)
 
d1 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 0}
d2 = {1: 1, 2: 2, 3: 3, 4: 5, 6: 2} 

#d1 = {1: 1}     
#d2 = {1: 1}
#Answer: ({1: True}, {})

#d1 = {0: 0, 2: 5, 5: 2}
#d2 = {0: 0, 2: 5}

#d1 = {1: 1, 2: 2, 3: 3}
#d2 = {1: 1, 2: 2, 3: 3}
#Answer = ({1: 0, 2: 0, 3: 0}, {})

#d1 = {1: 1, 2: 2, 3: 3}
#d2 = {1: 1, 2: 2, 3: 3}

#d1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 4}
#d2 = {1: 1, 2: 2, 3: 3, 4: 5}
# Correct Answer: ({1: False, 2: False, 3: False, 4: True}, {5: 4})
# My Answer: ({1: 2, 2: 4, 3: 6, 4: 9}, {5: 4})



print(dict_interdiff(d1, d2))


# Correct answer: ({1: True, 2: True, 3: True, 4: True}, {5: 0, 6: 2})
# Answer I'm getting: ({1: True, 2: True, 3: True, 4: True, 6: 2}, {5: 0, 6: 2})

