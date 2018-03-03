import random


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return


def compare(a, b, ascending=True, equality_check=True):
    if equality_check:
        if ascending and a <= b:
            return 1
        elif not ascending and a >= b:
            return 1
        else:
            return 0
    else:
        if ascending and a < b:
            return 1
        elif not ascending and a > b:
            return 1
        else:
            return 0


def swap_and_compare(list, i, j, ascending=True):
    if not compare(list[i], list[j], ascending):
        swap(list, i, j)
        return 1
    else:
        return 0


def bubble_sort(list, ascending=True):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            swap_and_compare(list, j, j+1, ascending)
    return


def insertion_sort(list, ascending=True):
    n=len(list)

    for i in range(1, n):
        k = i

        # get the position to place the element at
        # run the loop from i-1 to 0
        for j in reversed(range(i)):
            if compare(list[j], list[i], ascending):
                break
            k = j

        # shift the elements if needed
        if k != i:
            temp = list[i]
            for j in reversed(range(k, i)):
                list[j+1] = list[j]
            list[k] = temp
    return


def merge(list, start1, end1, start2, end2, ascending=True):
    merged_list = []
    if start1 > end1 or start2 > end2:
        return
    curr_list1 = start1
    curr_list2 = start2

    while curr_list1 <= end1 and curr_list2 <= end2:
        if compare(list[curr_list1], list[curr_list2], ascending):
            merged_list.append(list[curr_list1])
            curr_list1 += 1
        else:
            merged_list.append(list[curr_list2])
            curr_list2 += 1

    while curr_list1 <= end1:
        merged_list.append(list[curr_list1])
        curr_list1 += 1

    while curr_list2 <= end2:
        merged_list.append(list[curr_list2])
        curr_list2 += 1

    for i in range(0, len(merged_list)):
        list[start1+i] = merged_list[i]
    return


def _merge_sort(list, start, end, ascending=True):
    if start >= end:
        return

    mid = (start+end)//2
    _merge_sort(list, start, mid, ascending)
    _merge_sort(list, mid + 1, end, ascending)
    merge(list, start, mid, mid + 1, end, ascending)
    return




def merge_sort(list, ascending=True):
    n = len(list)
    _merge_sort(list, 0, n-1, ascending=ascending)


def partition(list, start, end, pivot, ascending=True):
    pivot_value = list[pivot]

    # print('Before', start, end, pivot_value, list)
    while start < end:
        if compare(pivot_value, list[start], ascending, True) and compare(list[end], pivot_value, ascending, True):
        # if list[start] >= pivot_value and list[end] <= pivot_value:
            swap(list, start, end)
        while start < end and compare(list[start], pivot_value, ascending, False):
        # while start < end and list[start] < pivot_value:
            start += 1
        # while start < end and list[end] > pivot_value:
        while start < end and compare(pivot_value, list[end], ascending, False):
            end -= 1

    return start

def _quick_sort(list, start, end, ascending=True):
    if start >= end:
        return

    # choose a pivot
    pivot = random.randint(start, end)

    pivot_index = partition(list, start, end, pivot, ascending=ascending)
    _quick_sort(list, start, pivot_index-1, ascending=ascending)
    _quick_sort(list, pivot_index + 1, end, ascending=ascending)


def quick_sort(list, ascending=True):
    n = len(list)

    _quick_sort(list, 0, n-1, ascending=ascending)


# quick_sort([1,2,3,4,5], False)
# quick_sort([5, 4, 3, 2, 1], True)
# quick_sort([50, 5, 4, 9, 10,8, 7, 11, 15, 19, 3, 2, 1, 21, 22, 100], True)
quick_sort([50, 5, 4, 9, 10,8, 7, 11, 15, 19, 3, 2, 1, 21, 22, 100], False)
# merge_sort([5, 4, 3, 2, 1], False)
# quick_sort([5, 4, 3, 2, 1], False)