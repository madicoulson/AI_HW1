print("hello")

#Quicksort
def quickSort(array):

    # creating 3 arrays to separate numbers into
    lowarr = []
    equalarr = []
    higharr = []

    # ensure array is not empty and more than 1 number
    if len(array) > 1:

        # taking the first number in the array to check other numbers against 
        checknum = array[0]

        # sorting the array based on groupings of larger, smaller, or equal to the checknum value
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


# hybridsort
def hybridSort(L, BIG, SMALL, T):
    # L = []
    if len(L) >= T:
        if isinstance(BIG, str):   
            if BIG == "mergeSort":
                mergeSort(L)
            elif BIG == "quickSort":
                quickSort(L)
            else:
                print("Error")
            return       
    else:
        if isinstance(SMALL, str):
            if SMALL == 'bubbleSort':
                bubbleSort(L)
            else:
                print("Error")
                return 


    
