import timeit

def time_sort(sort_func, arr, number):
    # the copy prevents the original array from being modified
    timer = timeit.Timer(lambda: sort_func(arr.copy())) 
    time_taken = timer.timeit(number=number)
    return time_taken / number  