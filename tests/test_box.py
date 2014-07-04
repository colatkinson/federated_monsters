#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_box
--------

Tests for `box` module.
"""

import unittest
import operator
from federated_monsters import box


class BoxTest(unittest.TestCase):

    """A unit test for the `box` module."""

    def test_respond(self):
        test_box = box.Box()
        out = [""]

        # Override the print_stream method so the test can use it.
        # Uses operator.setitem to get around inability to use assignments.
        test_box.print_stream = lambda y, z: operator.setitem(out, 0, z)
        test_box.respond_to_input(None, "hello world")
        print(out)

        self.assertEqual(out[0], "hello ['world']\n")
