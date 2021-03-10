import random

def partition(array, low, high):
    pivot = array[(low + high) // 2]

    left = low - 1
    right = high + 1
    while(True):

        left += 1
        while array[left] < pivot:
            left += 1

            
        right -= 1
        while array[right] > pivot:
            right -= 1

        
        if left >= right:
            return right
        
        array[left], array[right] = array[right], array[left]


def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        
        quicksort(array=array, low=low, high=pivot)
        quicksort(array=array, low=pivot+1, high=high)
    return

def randomized_partition(array, low, high):
    pivot = array[random.randint(low, high)]

    left = low - 1
    right = high + 1
    while(True):

        left += 1
        while array[left] < pivot:
            left += 1

            
        right -= 1
        while array[right] > pivot:
            right -= 1

        
        if left >= right:
            return right
        
        array[left], array[right] = array[right], array[left]

def randomized_quicksort(array, low, high):
    if low < high:
        pivot = randomized_partition(array, low, high)
        quicksort(array=array, low=low, high=pivot)
        quicksort(array=array, low=pivot+1, high=high)
    return

def qsort(array, mode='normal'):
    if mode == 'normal':
        quicksort(array, 0, len(array) -1)
    elif mode == 'randomized':
        randomized_quicksort(array, 0, len(array) -1)
    return array
    