#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AboutDictionaries(Koan):
    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        # self.assertEqual(__, len(empty_dict))
        self.assertEqual(0, len(empty_dict))    # dict() has nothing in it, answer zero



    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        # self.assertEqual(__, len(babel_fish))
        self.assertEqual(2, len(babel_fish)) # len(babel_fish) is looking for how many of the paired objects



    def test_accessing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        # self.assertEqual(__, babel_fish['one'])
        self.assertEqual('uno', babel_fish['one']) # we are looking for the value assigned to 'one'
        # self.assertEqual(__, babel_fish['two'])
        self.assertEqual('dos', babel_fish['two']) # we are looking for the value assigned to 'one'



    def test_changing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        babel_fish['one'] = 'eins'

        # expected = { 'two': 'dos', 'one': __ }
        # self.assertDictEqual(expected, babel_fish)

        expected = { 'two': 'dos', 'one': 'eins' }
        self.assertDictEqual(expected, babel_fish) # we reassigned 'one' from 'uno' to --> 'eins'



    def test_dictionary_is_unordered(self):
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual(True, dict1 == dict2)




    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(2, len(babel_fish.keys())) # length of the keys is 2 --> 'one' and 'two'
        self.assertEqual(2, len(babel_fish.values())) # length of the values is 2 --> 'uno' and 'dos'
        self.assertEqual(True, 'one' in babel_fish.keys()) # True --> 'one' is in babel_fish.keys
        self.assertEqual(False, 'two' in babel_fish.values()) # False --> 'two' is NOT in babel_fish.values
        self.assertEqual(False, 'uno' in babel_fish.keys()) # False --> 'uno' is NOT in babel_fish.keys
        self.assertEqual(True, 'dos' in babel_fish.values()) # True --> 'dos' is in babel_fish.values



    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(5, len(cards)) # asking for the length of the keys in cards, there are 5
        self.assertEqual(42, cards['green elf'])
        self.assertEqual(42, cards['yellow dwarf'])

