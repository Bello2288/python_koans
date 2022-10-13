#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

from runner.koan import *

class AboutLambdas(Koan):

# https://docs.quantifiedcode.com/python-anti-patterns/correctness/assigning_a_lambda_to_a_variable.html
# https://realpython.com/python-lambda/
# https://www.analyticsvidhya.com/blog/2020/03/what-are-lambda-functions-in-python/

    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        add_one = lambda n: n + 1
        # self.assertEqual(__, add_one(10))
        self.assertEqual(11, add_one(10))




    # ------------------------------------------------------------------

    def make_order(self, order):
        return lambda qty: str(qty) + " " + order + "s"

    def test_accessing_lambda_via_assignment(self):
        sausages = self.make_order('sausage')
        eggs = self.make_order('egg')

        # self.assertEqual(__, sausages(3))
        # self.assertEqual(__, eggs(2))
        self.assertEqual('3 sausages', sausages(3))
        self.assertEqual('2 eggs', eggs(2))

    def test_accessing_lambda_without_assignment(self):
        # self.assertEqual(__, self.make_order('spam')(39823))
        self.assertEqual('39823 spams', self.make_order('spam')(39823))
