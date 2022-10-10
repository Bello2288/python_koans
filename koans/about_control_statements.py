#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutControlStatements(Koan):

    def test_if_then_else_statements(self):
        if True:
            result = 'true value'
        else:
            result = 'false value'
        # self.assertEqual(__, result)
        self.assertEqual('true value', result)



    def test_if_then_statements(self):
        result = 'default value'
        if True:
            result = 'true value'
        # self.assertEqual(__, result)
        self.assertEqual('true value', result)



    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'
        # self.assertEqual(__, result)
        self.assertEqual('true value', result)



    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        # self.assertEqual(__, result)
        self.assertEqual(3628800, result) # (1 * 1, then 1 * 2, then 2 * 3, then 6 * 4, then 24 * 5,
                                          #   then 120 * 6, then 720 * 7, then 5,040 * 8, 
                                          #   then 40,320 * 9, then 362,880 * 10) which equals 3,628,800 0r 3628800



    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10: break
            result = result * i
            i += 1
        # self.assertEqual(__, result)
        self.assertEqual(3628800, result)



    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        # self.assertEqual(__, result)
        self.assertEqual([1, 3, 5, 7, 9], result)



    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase:
            result.append(item.upper())
        # self.assertEqual([__, __, __], result)
        self.assertEqual(['FISH', 'AND', 'CHIPS'], result)



    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or European Swallow?")
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")

        # text = __
        text = "Contestant: 'Robin'   Answer: 'Blue! I mean Green!'"

        self.assertRegex(result[2], text)

        self.assertNotRegex(result[0], text)
        self.assertNotRegex(result[1], text)
        self.assertNotRegex(result[3], text)
