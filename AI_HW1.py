print("hello")

#Quicksort
def quickSort(array):

    lowarr = []
    equalarr = []
    higharr = []

    if len(array) > 1:

        checknum = array[0]

        for x in array:
            if x < checknum:
                lowarr.append(x)
            if x == checknum:
                equalarr.append(x)
            if x > checknum:
                higharr.append(x)

        return quickSort(lowarr)+equalarr+quickSort(higharr)

    else:
        return array
      


    
