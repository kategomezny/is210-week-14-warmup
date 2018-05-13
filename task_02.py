#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests task 03."""

from data import FRUIT

def get_cost_per_item(shoplist):
    """Takes an argument(dict) and returns a new
    dictionary with the total cost per-item.

    Args:
        shoplist:  A dictionary.

    Return:  A dictionary

    Example:

    >>> get_cost_per_item({'Black Plum':2})
    {'Black Plum': 5.98}
    >>>

    """
    return {key:value * FRUIT[key] for key, value in shoplist.iteritems() if key in FRUIT}

def get_total_cost(shoplist):
    """Takes an argument(dict) and Returns the total cost.

     Args:
        shoplist:  A dictionary.

    Return:  A dictionary

    Example:

    >>> get_total_cost({'Black Plum':2,'Asian Pear':6})
    23.92
    >>>
    """
    return sum(get_cost_per_item(shoplist).values())
