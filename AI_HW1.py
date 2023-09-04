### bubbleSort
def bubbleSort(L):
    
    # Get the length, L, of the input list.
    length = len(L)
    
    # Local boolean flag to check if any values have been swapped while sorting.
    swapped = False
    
    for i in range(length-1):
        for k in range(0, length-i-1):
            # If the current value is larger than the next value, swap them.
            if L[k] > L[k+1]:
                swapped = True
                L[k], L[k+1] = L[k+1], L[k]
        
        # If nothing was swapped, just return the initial array, for it was already sorted.    
        if not swapped:
            return


### mergeSort
def mergeSort(L):
    
    # Check that the list has a length greater than 1
    if len(L) > 1:
        
        # Find the midpoint of the list, and split the list into left and right sections
        midpoint = len(L)//2
        left = L[:midpoint]
        right = L[midpoint:]
        
        # Recursively call mergeSort for the left and right sections
        mergeSort(left)
        mergeSort(right)
        
        # Set the three counter variables equal to 0
        i = 0
        j = 0
        k = 0
        
        # Check if the right or left section values are larger, and copy the 
        # smaller value to the initial list to sort
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1
        
        # Check if any elements are left over in either list, and if so,
        # add them to the initial list
        while i < len(left):
            L[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            L[k] = right[j]
            j += 1
            k += 1


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
   
            
### Testing:
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
arr2 = [64, 34, 25, 12, 22, 11, 90]
arr3 = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
mergeSort(arr2)
quickSort(arr3)

 
print("BUBBLE SORT Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
    
print("MERGE SORT Sorted array is:")
for i in range(len(arr2)):
    print("% d" % arr2[i], end=" ")

print("QUICK SORT Sorted array is:")
for i in range(len(arr3)):
    print("% d" % arr3[i], end=" ")

# Part 2:
# Quicksort as an agent- An agent with a divide and conquer architecture is the best option for quicksort because it is a pretty complex algorithm.
# The agent would keep breaking up the list into smaller parts recursively and then sorts and combines them.
# P- The best performance measure for quicksort would be the algorithms accuracy to sorting the list
# E- The environment would be the input and outputs of the algorithm. The input would be the unsorted list/array. 
# The output would be how the agent interacts with the input by rearranging the elements in the list to create the sorted list."
# A- The actuators would be the actual sorting actions used to change the list. This can include a pivot point or dividing up the list into those smalelr groups.
# S- The sensors would be the comparisons, swaps, and recursive calls needed to sort the list.

    
