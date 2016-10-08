import sys
def get_longest_subarray(lst, k):
    if not is_valid_inputs(lst, k):
        return None
    biggest_array, biggest_sum = [], -sys.maxint
    for i in xrange(1 << len(lst)):
        new_lst = [lst[j] for j in xrange(len(lst)) if (i & (1 << j))]
        new_lst_sum = sum(new_lst)
        if new_lst_sum <= k and len(biggest_array) < len(new_lst) and biggest_sum < new_lst_sum:
            biggest_array = new_lst
            biggest_sum = sum(biggest_array)
    return biggest_array
    
def is_valid_inputs(lst, k):
    if not isinstance(lst, list) or not lst or not isinstance(k, int) or k < 1:
        return False
    if any(not isinstance(item, int) for item in lst):
        return False
    return True

print get_longest_subarray([1, 2, 3, 4], 4)
