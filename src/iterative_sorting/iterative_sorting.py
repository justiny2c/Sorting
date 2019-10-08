# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for element in range(cur_index+1, len(arr)):
            if arr[element] < arr[smallest_index]:
                smallest_index = element
        # TO-DO: swap
        x = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = x

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # for _ in range(len(arr)):
    swap = True
    while swap:
        swap = False
        for element in range(0, len(arr)-1):
            if arr[element] > arr[element+1]:
                # x = arr[element+1]
                # arr[element+1] = arr[element]
                # arr[element] = x
                arr[element], arr[element+1] = arr[element+1], arr[element]
                swap = True

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


def quicksort(items):
    if len(items) <= 1:
        return items
    # 1. Select last element as the pivot
    pivot = items[-1]
    left = []
    right = []
    for i in range(len(items)-1)
      item = items[i]
       if item < pivot:  # 2. Move all elements smaller than the pivot to the left
            left.append(item)
        else:
            right.append(item)  # 3. Move all elements larget than the pivot to the right
    # 4. While LHS and RHS are greater than 1, repeats steps 1-3 on each
    return quicksort(left) + [pivot] + quicksort(right)
