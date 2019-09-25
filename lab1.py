def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    max = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > max:
            max = int_list[i]
    return max


def reverse_rec(int_list, rec_list = []):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    if int_list == []:
        return None
    rec_list.append(int_list.pop())
    return reverse_rec(int_list, rec_list)


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    pass
