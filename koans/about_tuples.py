#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutTuples(Koan):
    def test_creating_a_tuple(self):
        count_of_three =  (1, 2, 5)
        # self.assertEqual(__, count_of_three[2])   # Tuples are used to store multiple items in a single variable.
        self.assertEqual(5, count_of_three[2])   # 2 would indicate the index at position 2, which that number is 5



    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):
        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # Note, assertRegex() uses regular expression pattern matching,
        # so you don't have to copy the whole message.

        # self.assertRegex(msg, __)
        self.assertRegex(msg, "'tuple' object does not support item assignment")



    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three =  (1, 2, 5)
        # with self.assertRaises(___): count_of_three.append("boom")
        with self.assertRaises(AttributeError): count_of_three.append("boom")

        # Tuples are less flexible than lists, but faster.



    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)   # <--- makes a list of count_of_three, and was redefined as list_count
        list_count.append("boom")           # <--- .append will add to the end of a list, so "boom" is added 
        count_of_three = tuple(list_count)  # <--- turned list count into a tuple, and was redefined as count_of_three

        # self.assertEqual(__, count_of_three)
        self.assertEqual((1, 2, 5, "boom"), count_of_three)  # <-- asking for count_of_three so need to return with ( )



    def test_tuples_of_one_look_peculiar(self):             # https://python-textbok.readthedocs.io/en/1.0/Classes.html
        # self.assertEqual(__, (1).__class__)
        # self.assertEqual(__, (1,).__class__)
        # self.assertEqual(__, ("I'm a tuple",).__class__)
        # self.assertEqual(__, ("Not a tuple").__class__)
        self.assertEqual(int, (1).__class__)                # 1 is and integer
        self.assertEqual(tuple, (1,).__class__)             # 1,  the comma makes this a tuple
        self.assertEqual(tuple, ("I'm a tuple",).__class__) # the comma makes this a tuple because it comes after the str
        self.assertEqual(str, ("Not a tuple").__class__)    # because there is nothing else outside the " " it is a string



    def test_tuple_constructor_can_be_surprising(self):
        # self.assertEqual(__, tuple("Surprise!"))
        self.assertEqual(('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!'), tuple("Surprise!")) # <-- takes the string and 
                                                                                            # turns into a tuple



    def test_creating_empty_tuples(self):
        # self.assertEqual(__ , ())
        # self.assertEqual(__ , tuple()) #Sometimes less confusing
        self.assertEqual(() , ())
        self.assertEqual(() , tuple()) #Sometimes less confusing



    def test_tuples_can_be_embedded(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        # self.assertEqual(__, place)
        self.assertEqual(('Area 51', (37, 14, 6, 'N'), (115, 48, 40, 'W')), place)



    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        # self.assertEqual(__, locations[2][0])
        self.assertEqual("Cthulu", locations[2][0]) # start at index [2] which is ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W'))
                                                    # because this tuple was .append (added to the end).
                                                    # then going to the index of [0] which is "Cthulu"
                                                            
        # self.assertEqual(__, locations[0][1][2])
        self.assertEqual(15.56, locations[0][1][2]) # start at index [0] which is ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W'))
                                                    # going to the index of [1] in that tuple which is (38, 52, 15.56, 'N'),
                                                    # then going to the index of [2] which is 15.56