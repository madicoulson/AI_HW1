print("hello")

#Quicksort
def quickSort(L):

    # creating 3 arrays to separate numbers into
    lowarr = []
    equalarr = []
    higharr = []

    # ensure array is not empty and more than 1 number
    if len(L) > 1:

        # taking the first number in the array to check other numbers against 
        checknum = L[0]

        # sorting the array based on groupings of larger, smaller, or equal to the checknum value
        for x in L:
            if x < checknum:
                lowarr.append(x)
            if x == checknum:
                equalarr.append(x)
            if x > checknum:
                higharr.append(x)

        return quickSort(lowarr)+equalarr+quickSort(higharr)

    else:
        return L


# hybridsort
# taking in the parameters
def hybridSort(L, BIG, SMALL, T):
    # L = []
    # checking to see the length of the list to determine what algorithms to use
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


"Part 2:
"Quicksort as an agent- An agent with a divide and conquer architecture is the best option for quicksort because it is a pretty complex algorithm.
"The agent would keep breaking up the list into smaller parts recursively and then sorts and combines them.
"P- The best performance measure for quicksort would be the algorithms accuracy to sorting the list
"E- The environment would be the input and outputs of the algorithm. The input would be the unsorted list/array. 
"The output would be how the agent interacts with the input by rearranging the elements in the list to create the sorted list."
"A- The actuators would be the actual sorting actions used to change the list. This can include a pivot point or dividing up the list into those smalelr groups.
"S- The sensors would be the comparisons, swaps, and recursive calls needed to sort the list.

    
