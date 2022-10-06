#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        # self.assertEqual(__, names)

        self.assertEqual(["John", "Smith"], names) 
        # return the entire names list

# --------------------------------------------------------------------------------------       

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        # self.assertEqual(__, first_name)
        # self.assertEqual(__, last_name)

        self.assertEqual("John", first_name)
        # return just the first name
        self.assertEqual("Smith", last_name)
        # return just the last name

# --------------------------------------------------------------------------------------

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        # self.assertEqual(__, title)
        # self.assertEqual(__, first_names)
        # self.assertEqual(__, last_name)

        self.assertEqual("Sir", title)
        # return just the title
        self.assertEqual(['Ricky', 'Bobby'], first_names)
        # The * operator is known, in this context, as the tuple (or iterable) unpacking operator.
        # found at https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/
        # In this scenerio there needs to be enough values to unpack.
        #   we have three items and four values, so the * on first name will take the value of 
        #   two and three ('Ricky', 'Bobby') 
        self.assertEqual("Worthington", last_name)
        # return just the last name

# --------------------------------------------------------------------------------------

    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        # self.assertEqual(__, title)
        # self.assertEqual(__, first_names)
        # self.assertEqual(__, last_name)

        self.assertEqual("Mr", title)
        self.assertEqual([], first_names)
        self.assertEqual("Bond", last_name)
        # We have three items but only 2 values to unpack. title will be assigned the value of "Mr"
        #   and last name will take the last value which is "Bond". Since there is nothing for 
        #   *first_names it will have a value of an empty list []

# --------------------------------------------------------------------------------------

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        # self.assertEqual(__, first_name)
        # self.assertEqual(__, last_name)

        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)
        # first value is a combined value of "Willie", "Rae" so that will go with first_name
        #   and the last value will go to last_name

# --------------------------------------------------------------------------------------

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        # self.assertEqual(__, first_name)
        # self.assertEqual(__, last_name)

        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)
        #                first_name, last_name = last_name, first_name
        # original --->     Rob         Roy       but then first_name gets switch with last_name
        #   first_name, last_name = last_name, first_name
        #      Roy          Rob  |||   Roy         Rob
        #                               ^           ^
        #          new value of last_name          new value of first_name
