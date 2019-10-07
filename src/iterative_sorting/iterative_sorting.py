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
                print(f"Array element: {arr[element]}")
                smallest_index = element

        # TO-DO: swap
        x = arr[smallest_index]

        arr[smallest_index] = arr[i]
        arr[i] = x

    print(f"HELLO {arr}")
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
