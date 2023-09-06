### Group Members Names:
### Madilyn Coulson, Isabella Hall, Chloe Belletti

import time
import random


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
    lowList = []
    equalList = []
    highList = []

    # Ensure list is not empty and has more than 1 number
    if len(L) > 1:

        # Taking the first number in the list to check other numbers against 
        checkNum = L[0]

        # Sorting the list based on groupings of larger, smaller, or equal to the checkNum value
        for x in L:
            if x < checkNum:
                lowList.append(x)
            if x == checkNum:
                equalList.append(x)
            if x > checkNum:
                highList.append(x)

        # Recursively calling the functionality again until sorted
        return quickSort(lowList)+equalList+quickSort(highList)

    else:
        return L
    

### hybridSort
def hybridSort(L, BIG, SMALL, T):

    # Check to see the length of the list to determine which algorithms to use
    if len(L) >= T:   
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
            # Creating 3 lists to separate numbers into
            lowList = []
            equalList = []
            highList = []

            # Ensure list is not empty and has more than 1 number
            if len(L) > 1:

                # Taking the first number in the list to check other numbers against 
                checkNum = L[0]

                # Sorting the list based on groupings of larger, smaller, or equal to the checkNum value
                for x in L:
                    if x < checkNum:
                        lowList.append(x)
                    if x == checkNum:
                        equalList.append(x)
                    if x > checkNum:
                        highList.append(x)
                    
                # Recursively call hybridSort on both sides of the list
                hybridSort(lowList, "quickSort", "bubbleSort", T) 
                hybridSort(highList, "quickSort", "bubbleSort", T)
                L[:] = lowList + equalList + highList
                    
        else:
            print("Error")
        return       
    else:
        if SMALL == 'bubbleSort':
            bubbleSort(L)
        else:
            print("Error")
            return

def algorithmComparison(algorithm, randomList):
    
    if algorithm == mergeSort or algorithm == quickSort or algorithm == bubbleSort:
        start = time.time()
        algorithm(randomList)
        end = time.time()
        totalTime = end - start
        print(f'{algorithm} Total Time: {totalTime} seconds')
        
    elif algorithm == hybridSort:
        start = time.time()
        algorithm(randomList.copy(), "quickSort", "bubbleSort", len(randomList)//2)
        end = time.time()
        totalTime = end - start
        print(f'{algorithm} with quickSort Total Time: {totalTime} seconds')
        
        start2 = time.time()
        algorithm(randomList.copy(), "mergeSort", "bubbleSort", len(randomList)//2)
        end2 = time.time()
        totalTime2 = end2 - start2
        print(f'{algorithm} with mergeSort Total Time: {totalTime2} seconds')
        
                    
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
hybridSort(test1_arr4, "quickSort", "bubbleSort", 5)

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
for i in range(len(test1_arr4)):
    print("% d" % test1_arr4[i], end=" ")
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
hybridSort(test2_arr4, "quickSort", "bubbleSort", 2)

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
for i in range(len(test2_arr4)):
    print("% d" % test2_arr4[i], end=" ")
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
hybridSort(test3_arr4, "quickSort", "bubbleSort", 8)

 
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
for i in range(len(test3_arr4)):
    print("% d" % test3_arr4[i], end=" ")
print("\n")


# Test 4 - random list for time complexities
randomList = [random.randint(1, 1000) for _ in range(1000)]
algorithmComparison(bubbleSort, randomList)
algorithmComparison(quickSort, randomList)
algorithmComparison(mergeSort, randomList)
algorithmComparison(hybridSort, randomList)


### Part 2:
# Quicksort as an agent- An agent with a divide and conquer architecture is the best option for quicksort because it is a pretty complex algorithm.
# The agent would keep breaking up the list into smaller parts recursively and then sorts and combines them.
# P- The best performance measure for quicksort would be the algorithms accuracy to sorting the list
# E- The environment would be the input and outputs of the algorithm. The input would be the unsorted list/array. 
# The output would be how the agent interacts with the input by rearranging the elements in the list to create the sorted list."
# A- The actuators would be the actual sorting actions used to change the list. This can include a pivot point or dividing up the list into those smalelr groups.
# S- The sensors would be the comparisons, swaps, and recursive calls needed to sort the list.


# Bubblesort as an agent- It could be a reflex agent becasue it repeatedly compares and swaps elements until the entire list is sorted and its a simple algorithm. 
# P- Some performance measures would include both efficency and accuracy, so measuring both the time and how accuarate the list was sorted. 
# E- The environment would again be the input and output of the unsorted versus sorted list. 
# A- Operation of just comparing each element and swapping them if needed 
# S- The comparison results of whether or not it needs to be swapped 


# Mergesort as an agent- An agent with a divide and conquer architecture is the best option for mergesort because it is a recursive algorithm
# P- Performance measures for mergesort include complexity, run time, and accuracy
# E- The environment would be the I/O of the algorithm
# A- The actuators would be the operations taking place in the function that actually sort the list
# S- The sensors would be the comparisons, recursive calls, and logic blocks needed to sort the list.


# Discussion Comparing the Four Algorithms
# Below is the date after running the algorithmComparison method above three times.

# Trial 1:
# <function bubbleSort at 0x000002E484A4DF80> Execution Time: 0.03461146354675293 seconds
# <function quickSort at 0x000002E484A4E520> Execution Time: 0.018617868423461914 seconds
# <function mergeSort at 0x000002E484A4E3E0> Execution Time: 0.0010008811950683594 seconds
# <function hybridSort at 0x000002E484A9C360> with quickSort Execution Time: 0.014557600021362305 seconds
# <function hybridSort at 0x000002E484A9C360> with mergeSort Execution Time: 0.000982046127319336 seconds

# Trial 2:
# <function bubbleSort at 0x0000017BFDC3DF80> Execution Time: 0.02999734878540039 seconds
# <function quickSort at 0x0000017BFDC3E520> Execution Time: 0.017022371292114258 seconds
# <function mergeSort at 0x0000017BFDC3E3E0> Execution Time: 0.0010013580322265625 seconds
# <function hybridSort at 0x0000017BFDC8C360> with quickSort Execution Time: 0.013017416000366211 seconds
# <function hybridSort at 0x0000017BFDC8C360> with mergeSort Execution Time: 0.0009834766387939453 seconds

# Trial 3:
# <function bubbleSort at 0x000002405CFEDF80> Execution Time: 0.033535003662109375 seconds
# <function quickSort at 0x000002405CFEE520> Execution Time: 0.020998239517211914 seconds
# <function mergeSort at 0x000002405CFEE3E0> Execution Time: 0.0010247230529785156 seconds
# <function hybridSort at 0x000002405D03C360> with quickSort Execution Time: 0.01697373390197754 seconds
# <function hybridSort at 0x000002405D03C360> with mergeSort Execution Time: 0.000997781753540039 seconds

# According the the date above, the order of most to least efficient is as follows, with 1 being the most efficient:
# 1. hybridSort calling mergeSort
# 2. mergeSort
# 3. hybridSort calling quickSort
# 4. quickSort
# 5. bubbleSort

# This is logical due to the sorting operations in each of the methods.

