#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        # self.assertEqual(__, string)
        self.assertEqual("The values are one and 2", string) # values1 is the {0} index and value2 is the {1} index



    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        # self.assertEqual(__, string)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)



    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        # self.assertEqual(__, string)
        self.assertEqual("The square root of 5 is 2.2361", string) # math.sqrt(5) is the index of {0} and the the :. will
                                                                   # input the decimal, then the '2361 is the value of {1}



    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("let", string[7:10]) #"B  a  c  o  n  ,     l  e  t  t   u   c   e        a  n  d    t  o  m  a  t  o"
                                              # ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^   ^   ^   ^   ^    ^  ^  ^  ^ ^  ^  ^  ^  ^  ^
                                     # indexes  0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15.....
                                    # string [7:10] we are starting at index of 7, going up to but not including 10
                                                                        # ^
                                                                        # ^
    def test_you_can_get_a_single_character_from_a_string(self):        # ^
        string = "Bacon, lettuce and tomato"                            # ^
        # self.assertEqual(__, string[1])                               # ^
        self.assertEqual("a", string[1]) #  string [1] we are starting at index of 1, which is "a"



    def test_single_characters_can_be_represented_by_integers(self):
        # self.assertEqual(__, ord('a'))
        # self.assertEqual(__, ord('b') == (ord('a') + 1))
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1)) # ord('b') = 98 ----> so 97 + 1 is 98
 


    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        # self.assertListEqual([__, __, __], words)
        self.assertListEqual(['Sausage', 'Egg', 'Cheese'], words) # split will seperate eacg item in the string



    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        # self.assertListEqual([__, __, __, __], words)
        self.assertListEqual(['the', 'rain', 'in', 'spain'], words) # https://interactivechaos.com/en/python/function/recompile

        # Pattern is a Python regular expression pattern which matches ',' or ';'



    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        # self.assertEqual(__, string)
        # self.assertEqual(__, len(string))
        self.assertEqual('\\n', string) # the r adds and extra \ to \n ---> makes \\n
        self.assertEqual(2, len(string)) # \n is 2 characters

        # Useful in regular expressions, file paths, URLs, etc.



    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        # self.assertEqual(__, ' '.join(words))
        self.assertEqual("Now is the time", ' '.join(words)) # taking the words and joining together with a space --> ' '



    def test_strings_can_change_case(self):
        # self.assertEqual(__, 'guido'.capitalize())
        # self.assertEqual(__, 'guido'.upper())
        # self.assertEqual(__, 'TimBot'.lower())
        # self.assertEqual(__, 'guido van rossum'.title())
        # self.assertEqual(__, 'ToTaLlY aWeSoMe'.swapcase())
        self.assertEqual('Guido', 'guido'.capitalize()) # this will take the string and capitalize the first letter
        self.assertEqual('GUIDO', 'guido'.upper()) # this will take the string and make every letter uppercase
        self.assertEqual('timbot', 'TimBot'.lower()) # this will take the string and make every letter lowercase
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())        # this will take the string and upper case 
                                                                                  # the first letter in each word
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase()) # this will take the string and swap the uppercase
                                                                          # letters to lowercase, and vise versa.
