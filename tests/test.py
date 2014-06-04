#!/usr/bin/env python
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view


class TestCase(unittest.TestCase):
    '''
    Test module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module(
            'sale_opportunity_next_action')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('sale_opportunity_next_action')


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
    return suite
