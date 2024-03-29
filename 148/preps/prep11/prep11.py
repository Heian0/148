"""Prep 11 Synthesize: Recursive Sorting Algorithms

=== CSC148 Summer 2021 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu and Diane Horton

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 David Liu and Diane Horton

=== Module Description ===
This file includes the recursive sorting algorithms from this week's prep
readings, and two short programming exercises to extend your learning about
these algorithms in different ways.
"""
import random
from typing import Any


################################################################################
# Mergesort and Quicksort
################################################################################
def mergesort(lst: list) -> list:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.

    >>> mergesort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        # Merge the two sorted halves. Need a helper here!
        return _merge(left_sorted, right_sorted)


def _merge(lst1: list, lst2: list) -> list:
    """Return a sorted list with the elements in <lst1> and <lst2>.

    Precondition: <lst1> and <lst2> are sorted.
    """
    index1 = 0
    index2 = 0
    merged = []
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            merged.append(lst1[index1])
            index1 += 1
        else:
            merged.append(lst2[index2])
            index2 += 1

    # Now either index1 == len(lst1) or index2 == len(lst2).

    # The remaining elements of the other list
    # can all be added to the end of <merged>.
    # Note that at most ONE of lst1[index1:] and lst2[index2:]
    # is non-empty, but to keep the code simple, we include both.
    return merged + lst1[index1:] + lst2[index2:]


def quicksort(lst: list) -> list:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.

    >>> quicksort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Pick pivot to be first element.
        # Could make lots of other choices here (e.g., last, random)
        pivot = lst[0]

        # Partition rest of list into two halves
        smaller, bigger = _partition(lst[1:], pivot)

        # Recurse on each partition
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # Return! Notice the simple combining step
        return smaller_sorted + [pivot] + bigger_sorted


def _partition(lst: list, pivot: Any) -> tuple[list, list]:
    """Return a partition of <lst> with the chosen pivot.

    Return two lists, where the first contains the items in <lst>
    that are <= pivot, and the second is the items in <lst> that are > pivot.
    """
    smaller = []
    bigger = []

    for item in lst:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)

    return smaller, bigger


################################################################################
# Synthesize exercises
################################################################################
def mergesort3(lst: list) -> list:
    """Return a sorted version of <lst> using three-way mergesort.

    Three-way mergesort is similar to mergesort, except:
        - it divides the input list into *three* lists of (almost) equal length
        - the main helper merge3 takes in *three* sorted lists, and returns
          a sorted list that contains elements from all of its inputs.

    HINT: depending on your implementation, you might need another base case
    when len(lst) == 2 to avoid an infinite recursion error.

    >>> mergesort3([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst[:]

    if len(lst) == 2:
        if lst[0] > lst[1]:
            temp = lst[0]
            lst[0] = lst[1]
            lst[1] = temp
            return lst[:]
        return lst[:]

    else:
        index = len(lst) // 3
        first_sorted = mergesort3(lst[:index])
        second_sorted = mergesort3(lst[index:(2 * index)])
        third_sorted = mergesort3(lst[(2 * index):])

        return merge3(first_sorted, second_sorted, third_sorted)


def merge3(lst1: list, lst2: list, lst3: list) -> list:
    """Return a sorted list with the elements in the given input lists.

    Precondition: <lst1>, <lst2>, and <lst3> are all sorted.

    This *must* be implemented using the same approach as _merge; in particular,
    it should use indexes to keep track of where you are in each list.
    This will keep your implementation efficient, which we will be checking for.

    Since this involves some detailed work with indexes, we recommend splitting
    up your code into one or more helpers to divide up (and test!) each part
    separately.
    """
    index1 = 0
    index2 = 0
    index3 = 0
    merged = []

    while index1 < len(lst1) and index2 < len(lst2) and index3 < len(lst3):
        if lst1[index1] <= lst2[index2] and lst1[index1] <= lst3[index3]:
            merged.append(lst1[index1])
            index1 += 1

        elif lst2[index2] <= lst1[index1] and lst2[index2] <= lst3[index3]:
            merged.append(lst2[index2])
            index2 += 1

        elif lst3[index2] <= lst1[index1] and lst3[index3] <= lst2[index2]:
            merged.append(lst3[index3])
            index3 += 1

    if index1 >= len(lst1):
        while index2 < len(lst2) and index3 < len(lst3):
            if lst2[index2] <= lst3[index3]:
                merged.append(lst2[index2])
                index2 += 1

            else:
                merged.append(lst3[index3])
                index3 += 1

    if index2 >= len(lst2):
        while index1 < len(lst1) and index3 < len(lst3):
            if lst1[index1] <= lst3[index3]:
                merged.append(lst1[index1])
                index1 += 1
            else:
                merged.append(lst3[index3])
                index3 += 1
    if index3 >= len(lst3):
        while index1 < len(lst1) and index2 < len(lst2):
            if lst1[index1] <= lst2[index2]:
                merged.append(lst1[index1])
                index1 += 1
            else:
                merged.append(lst2[index2])
                index2 += 1

    return merged + lst1[index1:] + lst2[index2:] + lst3[index3:]


def kth_smallest(lst: list, k: int) -> Any:
    """Return the <k>-th smallest element in <lst>.

    Raise IndexError if k < 0 or k >= len(lst).
    Note: for convenience, k counts from 0, so kth_smallest(lst, 0) == min(lst).

    Precondition: <lst> does not contain duplicates.

    >>> kth_smallest([10, 20, -4, 3], 0)
    -4
    >>> kth_smallest([10, 20, -4, 3], 2)
    10
    """
    if k < 0 or k >= len(lst):
        raise ValueError

    if len(lst) == 1:
        return lst[0]

    pivot = lst[random.randint(0, len(lst) - 1)]

    partition = _partition(lst, pivot)
    smaller, bigger = partition[0], partition[1]

    if len(smaller) - 1 >= k:
        return kth_smallest(smaller, k)

    else:
        return kth_smallest(bigger, k - len(smaller))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={'disable': ['E1136']})
