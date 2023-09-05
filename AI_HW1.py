### Group Members Names:
### Madilyn Coulson, Isabella Hall, Chloe Belletti


### bubbleSort
def bubbleSort(L):
    
    # Get the length, L, of the input list.
    length = len(L)
    
    # Check that the list has a length greater than 1
    if length > 1:
    
        # Local boolean flag to check if any values have been swapped while sorting
        swapped = False

        for i in range(length-1):
            for k in range(0, length-i-1):
                # If the current value is larger than the next value, swap them
                if L[k] > L[k+1]:
                    swapped = True
                    L[k], L[k+1] = L[k+1], L[k]
            
            # If nothing was swapped, just return the initial array, for it was already sorted    
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


### quickSort
def quickSort(L):

    # Creating 3 lists to separate numbers into
    lowarr = []
    equalarr = []
    higharr = []

    # Ensure list is not empty and has more than 1 number
    if len(L) > 1:

        # Taking the first number in the list to check other numbers against 
        checknum = L[0]

        # Sorting the list based on groupings of larger, smaller, or equal to the checknum value
        for x in L:
            if x < checknum:
                lowarr.append(x)
            if x == checknum:
                equalarr.append(x)
            if x > checknum:
                higharr.append(x)

        # Recursively calling the functionality again until sorted
        return quickSort(lowarr)+equalarr+quickSort(higharr)

    else:
        return L


### hybridSort
def hybridSort(L, BIG, SMALL, T):

    # Check to see the length of the list to determine which algorithms to use
    if len(L) >= T:
        if isinstance(BIG, str):   
            if BIG == "mergeSort":
                
                # Find the midpoint of the list, and split the list into left and right sections
                midpoint = len(L)//2
                left = L[:midpoint]
                right = L[midpoint:]
                
                # Recursively call hybridSort on both sides of the list
                hybridSort(left, "mergeSort", "bubbleSort", T)
                hybridSort(right, "mergeSort", "bubbleSort", T)
                
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
                
            elif BIG == "quickSort":
                def quickSorts(L):
                    if len(L) <= 1:
                        return L
                
                    pivot = L[len(L) // 2]  # Choose a pivot element
                    left = [x for x in L if x < pivot]
                    middle = [x for x in L if x == pivot]
                    right = [x for x in L if x > pivot]
                
                    return quickSorts(left) + middle + quickSorts(right)
            
                L = quickSorts(L)  # Call quickSort function
            else:
                print("Error")
            return L
    else:
        if isinstance(SMALL, str):
            if SMALL == 'bubbleSort':
                bubbleSort(L)
            else:
                print("Error")
                return 
   
            
### Testing Code:

# Test 1 - list with 7 values
test1_arr = [25, 98, 16, 2, 57, 23, 71]
test1_arr2 = [25, 98, 16, 2, 57, 23, 71]
test1_arr3 = [25, 98, 16, 2, 57, 23, 71]
test1_arr4 = [25, 98, 16, 2, 57, 23, 71]

print("Test 1: Initial Array")
for i in range(len(test1_arr)):
    print("% d" % test1_arr[i], end=" ")
print("\n")
 
bubbleSort(test1_arr)
mergeSort(test1_arr2)
quickSortList1 = quickSort(test1_arr3)
hybridSort(test1_arr3, "mergeSort", "bubbleSort", 5)
hybridSortList1 = hybridSort(test1_arr4, "quickSort", "bubbleSort", 5)

print("Test 1: Bubble Sorted List Output:")
for i in range(len(test1_arr)):
    print("% d" % test1_arr[i], end=" ")
print("\n")
    
print("Test 1: Merge Sorted List Output:")
for i in range(len(test1_arr2)):
    print("% d" % test1_arr2[i], end=" ")
print("\n")

print("Test 1: Quick Sorted List Output:")
for i in range(len(quickSortList1)):
    print("% d" % quickSortList1[i], end=" ")
print("\n")

print("Test 1: Hybrid Sorted List Output MergeSort:")
for i in range(len(test1_arr3)):
    print("% d" % test1_arr3[i], end=" ")
print("\n")

print("Test 1: Hybrid Sorted List Output QuickSort:")
for i in range(len(hybridSortList1)):
    print("% d" % hybridSortList1[i], end=" ")
print("\n")


# Test 2 - list with 3 values
test2_arr = [61, 34, 12]
test2_arr2 = [61, 34, 12]
test2_arr3 = [61, 34, 12]
test2_arr4 = [61, 34, 12]


print("Test 2: Initial Array")
for i in range(len(test2_arr)):
    print("% d" % test2_arr[i], end=" ")
print("\n")
 
bubbleSort(test2_arr)
mergeSort(test2_arr2)
quickSortList2 = quickSort(test2_arr3)
hybridSort(test2_arr3, "mergeSort", "bubbleSort", 2)
hybridSortList2 = hybridSort(test2_arr4, "quickSort", "bubbleSort", 2)

print("Test 2: Bubble Sorted Array Output:")
for i in range(len(test2_arr)):
    print("% d" % test2_arr[i], end=" ")
print("\n")
    
print("Test 2: Merge Sorted array is:")
for i in range(len(test2_arr2)):
    print("% d" % test2_arr2[i], end=" ")
print("\n")

print("Test 2: Quick Sorted array is:")
for i in range(len(quickSortList2)):
    print("% d" % quickSortList2[i], end=" ")
print("\n")

print("Test 2: Hybrid Sorted List Output MergeSort:")
for i in range(len(test2_arr3)):
    print("% d" % test2_arr3[i], end=" ")
print("\n")

print("Test 2: Hybrid Sorted List Output QuickSort:")
for i in range(len(hybridSortList2)):
    print("% d" % hybridSortList2[i], end=" ")
print("\n")


# Test 3 - list with 15 values
test3_arr = [71, 28, 90, 78, 5, 20, 16, 56, 89, 38, 14, 45, 26, 39, 76]
test3_arr2 = [71, 28, 90, 78, 5, 20, 16, 56, 89, 38, 14, 45, 26, 39, 76]
test3_arr3 = [71, 28, 90, 78, 5, 20, 16, 56, 89, 38, 14, 45, 26, 39, 76]
test3_arr4 = [71, 28, 90, 78, 5, 20, 16, 56, 89, 38, 14, 45, 26, 39, 76]

print("Test 3: Initial Array")
for i in range(len(test3_arr)):
    print("% d" % test3_arr[i], end=" ")
print("\n")
 
bubbleSort(test3_arr)
mergeSort(test3_arr2)
quickSortList3 = quickSort(test3_arr3)
hybridSort(test3_arr3, "mergeSort", "bubbleSort", 8)
hybridSortList3 = hybridSort(test3_arr4, "quickSort", "bubbleSort", 8)

 
print("Test 3: Bubble Sorted Array Output:")
for i in range(len(test3_arr)):
    print("% d" % test3_arr[i], end=" ")
print("\n")
    
print("Test 3: Merge Sorted array is:")
for i in range(len(test3_arr2)):
    print("% d" % test3_arr2[i], end=" ")
print("\n")

print("Test 3: Quick Sorted array is:")
for i in range(len(quickSortList3)):
    print("% d" % quickSortList3[i], end=" ")
print("\n")

print("Test 3: Hybrid Sorted List Output MergeSort:")
for i in range(len(test3_arr3)):
    print("% d" % test3_arr3[i], end=" ")
print("\n")

print("Test 3: Hybrid Sorted List Output QuickSort:")
for i in range(len(hybridSortList3)):
    print("% d" % hybridSortList3[i], end=" ")
print("\n")






# Part 2:
# Quicksort as an agent- An agent with a divide and conquer architecture is the best option for quicksort because it is a pretty complex algorithm.
# The agent would keep breaking up the list into smaller parts recursively and then sorts and combines them.
# P- The best performance measure for quicksort would be the algorithms accuracy to sorting the list
# E- The environment would be the input and outputs of the algorithm. The input would be the unsorted list/array. 
# The output would be how the agent interacts with the input by rearranging the elements in the list to create the sorted list."
# A- The actuators would be the actual sorting actions used to change the list. This can include a pivot point or dividing up the list into those smalelr groups.
# S- The sensors would be the comparisons, swaps, and recursive calls needed to sort the list.

    
