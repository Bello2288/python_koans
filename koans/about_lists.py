#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list)) # type of empty_list is a list
        self.assertEqual(0, len(empty_list))  # current length of the list is zero


# --------------------------------------------------------------------------------------

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)  # <----- .append will add the 333 to the end of the list
        self.assertListEqual([1, 2, 333], nums)


# --------------------------------------------------------------------------------------


    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        # index    0         1        2       3     ##
        # index   -4        -3      -2      -1      ##
        self.assertEqual('peanut', noms[0]) # display index 0
        self.assertEqual('jelly', noms[3]) # display index 3
        self.assertEqual('jelly', noms[-1]) # display index -1
        self.assertEqual('butter', noms[-3]) # display index -3


# --------------------------------------------------------------------------------------

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(["peanut"], noms[0:1])             #\
        self.assertEqual(["peanut", "butter"], noms[0:2])   # \
        self.assertEqual([], noms[2:2])                     #  found info at https://www.geeksforgeeks.org/python-list-slicing/
        self.assertEqual(["and", "jelly"], noms[2:20])      # /
        self.assertEqual([], noms[4:0])                     #/
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])


# --------------------------------------------------------------------------------------

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(["and", "jelly"], noms[2:])
         # ^^ this would read, start at index 2 and leave the rest of the list
        self.assertEqual(["peanut", "butter"], noms[:2])
        # ^^ this would read, start at the beginning and go up to but not include index 2


# --------------------------------------------------------------------------------------

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5))) # type of "range" is a range
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6)) 
        # this range will start at the number 1 and up to but not including 6
        self.assertEqual([0, 1, 2, 3, 4], list(range(5))) 
        # this range will give a range of 5 number starting at zero
        self.assertEqual([5, 6, 7, 8], list(range(5, 9))) 
        # this range will start at the number 5 and up to but not including 9

# --------------------------------------------------------------------------------------

    def test_ranges_with_steps(self):
        self.assertEqual([5, 4], list(range(5, 3, -1)))
    # this range will start at the number 5, up to but not including 3, and stepping backwards by 1 number
        self.assertEqual([0, 2, 4, 6], range(0, 8, 2))
    # this range will start at the number 2, up to but not including 8, stepping 2 numbers
        self.assertEqual([1, 4, 7], range(1, 8, 3))
    # this range will start at the number 1, up to but not including 8, stepping 3 numbers
        self.assertEqual([5, 1, -3], range(5, -7, -4))
    # this range will start at the number 5, up to but not including -7, stepping backwards by 3 number
        self.assertEqual([5, 1, -3, -7], range(5, -8, -4))
    # this range will start at the number 5, up to but not including -8, stepping backwards by 4 number
    


# --------------------------------------------------------------------------------------

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(__, knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(__, knight)


# --------------------------------------------------------------------------------------

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual(__, stack)

        popped_value = stack.pop()
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        popped_value = stack.pop(1)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)


# --------------------------------------------------------------------------------------

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual(__, queue)

        popped_value = queue.pop(0)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

