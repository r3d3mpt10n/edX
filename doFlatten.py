def flatten(aList):

    if isinstance(aList, list):
        if len(aList) == 0:
            return []
        x, y = aList[0], aList[1:]
        return flatten(x) + flatten(y)
    else:
        return [aList]
	    


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(list(aList)))	
