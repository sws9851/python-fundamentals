def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    # first element as pivot, per the spec; on already-sorted input that peels off
    # one item per call and recurses as deep as the list is long
    pivot = array[0]
    less = []
    equal = []
    more = []

    for item in array:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            equal.append(item)

    return quick_sort(less) + equal + quick_sort(more)


if __name__ == "__main__":
    print(quick_sort([33, 1, 89, 2, 67, 245]))
    print(quick_sort([4, 4, 4, 1, 1, 9, 9, 9]))
    print(quick_sort([]))
