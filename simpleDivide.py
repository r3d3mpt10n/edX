def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):

    try:
        return item / denom
    except ZeroDivisionError as e:
        return 0


list = [0, 2, 4]

print(FancyDivide(list, 0))
