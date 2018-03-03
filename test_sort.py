from sort import bubble_sort, insertion_sort, merge_sort, quick_sort


def check_sorted_order(list, ascending=True):
    for i in range(len(list) - 1):
        if ascending:
            assert list[i+1] >= list[i]
        else:
            assert list[i + 1] <= list[i]


def _test_sorted_order(func):
    list = [1, 2, 3, 4, 5]
    func(list, True)
    check_sorted_order(list, True)

    func(list, False)
    check_sorted_order(list, False)

    list = [5, 4, 3, 2, 1]
    func(list, True)
    check_sorted_order(list, True)

    func(list, False)
    check_sorted_order(list, False)

    list = [5, 4, 3, 2, 7]
    func(list, True)
    check_sorted_order(list, True)

    list = [5, 4, 3, 2, 7]
    func(list, False)
    check_sorted_order(list, False)

    list = [10, 9, 3, 2, 7]
    func(list, True)
    check_sorted_order(list, True)

    list = [10, 9, 3, 2, 7]
    func(list, False)
    check_sorted_order(list, False)

    list = []
    func(list, True)
    check_sorted_order(list, True)

    list = [100, 50, 22, 21, 19, 15, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1]
    func(list, True)
    check_sorted_order(list, True)

    list = [100, 50, 22, 21, 19, 15, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1]
    func(list, False)
    check_sorted_order(list, False)


def test_bubble_sort():
    _test_sorted_order(bubble_sort)


def test_insertion_sort():
    _test_sorted_order(insertion_sort)


def test_merge_sort():
    _test_sorted_order(merge_sort)


def test_quick_sort():
    _test_sorted_order(quick_sort)