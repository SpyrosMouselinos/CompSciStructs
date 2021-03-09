from comp_modules.Heap import PriorityHeap

test_iterable = [6,4,8,1,5,2,3,14,9,7,10,15,11,20]


def test_creation_and_sort():
    myHeap = PriorityHeap(mode='max', name='TestMaxHeap')
    myHeap.heapFromIterable(test_iterable)
    for i in range(0, len(myHeap.heap)):
        if myHeap.leftChildOf(i) is not None:
            assert myHeap.heap[i] > myHeap.leftChildOf(i)
        if myHeap.rightChildOf(i) is not None:
            assert myHeap.heap[i] > myHeap.rightChildOf(i)
    myHeap.heapsort(myHeap.heap)
    sorted(myHeap.heap) == myHeap.heap
    return

