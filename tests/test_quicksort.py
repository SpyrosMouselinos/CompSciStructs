from random import randint
from timeit import default_timer as timer
from comp_modules.Quicksort import qsort

test_iterable = [3,2,1,7,5,6,4,8,10,9,20,10,35]


def test_and_compare_sorts():
    assert qsort(test_iterable, mode='normal') == sorted(test_iterable)
    assert qsort(test_iterable, mode='randomized') == sorted(test_iterable)
    return


def test_speed_of_sorts():
    test_array_small  = [randint(0,100) for _ in range(0,20)]
    test_array_medium = [randint(0,100) for _ in range(0,1000)]
    test_array_large  = [randint(0,100) for _ in range(0,10000)]
    def perform_timetest(mode, test):
        start = timer()
        qsort(test, mode=mode)
        end = timer()
        return round(end - start, 4)
    
    assert perform_timetest('normal', test_array_small) >= perform_timetest('randomized', test_array_small)
    assert perform_timetest('normal', test_array_medium) >= perform_timetest('randomized', test_array_medium)
    assert perform_timetest('normal', test_array_large) >= perform_timetest('randomized', test_array_large)
    return