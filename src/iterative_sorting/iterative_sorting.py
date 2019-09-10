# TO-DO: Complete the selection_sort() function below 


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # finds next smallest element
        for j in range(current_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]
             
    print(arr)
    return arr
    

#import random
#arr = list(range(10))
#random.shuffle(arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    has_swapped = True
    #when no swaps have occured 
    while has_swapped:
        has_swapped = False
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i+1]:
                #swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
    print(arr)
    return arr
    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr