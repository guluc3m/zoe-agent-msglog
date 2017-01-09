# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *

def traverse(intent, inner, depth = 0):
    margin = '  ' * depth
    margin2 = '  ' * (depth + 1)
    keys = sorted(intent)
    if intent == inner:
        print('\033[92m', end = '')
    print(margin + '{')
    for key in keys:
        value = intent[key]
        if isinstance(value, dict):
            print(margin2 + key + ':', end = '')
            traverse(value, inner, depth + 1)
        elif isinstance(value, list):
            print(margin2 + key + ': [')
            for p in value:
                traverse(p, inner, depth + 2)
            print(margin2 + ']')
        elif isinstance(value, str):
            print(margin2 + key + ':', '"' + value + '"')
        else:
            print(margin2 + key + ':', value)
    print(margin + '}')
    if intent == inner:
        print('\033[0m', end = '')



@Agent('Log')
class LogAgent:

    @Any()
    @Raw()
    def x(self, intent):
        inner = IntentTools.inner_intent(intent)
        traverse(intent, inner)
        print()
