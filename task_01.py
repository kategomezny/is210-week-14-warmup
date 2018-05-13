#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests task 03."""

from pet import Pet

class Dog(Pet):
    def __init__(self, has_shots=False, **args):
        """constructor for the Dog class.

        Args:
            has_shots: (boolean, optional), Defaults to False

            **args: arbitrary arguments dictionary
        """            
        self.has_shots = has_shots
        super(Dog, self).__init__(**args)
