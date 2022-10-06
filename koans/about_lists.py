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

        self.assertEqual(["peanut"], noms[0:1])             
        # this will slice at the index of zero, and go up to but not include index 1
        self.assertEqual(["peanut", "butter"], noms[0:2])   
        # this will slice at the index of zero, and go up to but not include index 2
        self.assertEqual([], noms[2:2])                     
        #  this will slice at the index of 2, and go up to but not include index 2, so it will return an empty list
        self.assertEqual(["and", "jelly"], noms[2:20])      
        # this will slice at the index of 2, and go up to but not include index 20, so will return only what is available
        self.assertEqual([], noms[4:0])                     
        # this will slice at the index of 4, since there is no index of 4, we return an empy list
        self.assertEqual([], noms[4:100])
        # this will slice at the index of 4, since there is no index of 4, we return an empy list
        self.assertEqual([], noms[5:0])
        # this will slice at the index of 5, since there is no index of 5, we return an empy list


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
        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
    # this range will start at the number 2, up to but not including 8, stepping 2 numbers
        self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
    # this range will start at the number 1, up to but not including 8, stepping 3 numbers
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
    # this range will start at the number 5, up to but not including -7, stepping backwards by 3 number
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))
    # this range will start at the number 5, up to but not including -8, stepping backwards by 4 number
    


# --------------------------------------------------------------------------------------

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)
        # this will insert the string 'not' into the second index position ['you', 'shall', ^^, 'pass'] and make 'pass' the tird index
        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)
        # this will take the new knight and insert the string 'Arthur' into the zero index position 

# --------------------------------------------------------------------------------------

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)
        # stack.append('last') will insert and string 'last' to the end of the list

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        # the empty pop() method will remove the last added item, in this case it was 'last'
        self.assertEqual([10, 20, 30, 40], stack)
        # the new stack value is [10, 20, 30, 40]

        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        # stack.pop(1) will remove the item from the first index which is 20
        self.assertEqual([10, 30, 40], stack)
        # the new stack value is [10, 30, 40]

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)


# --------------------------------------------------------------------------------------

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual([1, 2, 'last'], queue)

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

