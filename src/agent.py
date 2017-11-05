# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *

def traverse(intent, inner, depth = 0, color = '\033[0m', skipMargin = False):
    if intent == inner:
        color = '\033[92m'
    margin = color + '  ' * depth
    margin2 = color + '  ' * (depth + 1)
    keys = sorted(intent)
    if skipMargin:
        print(color + '{')
    else:
        print(margin + '{')
    for key in keys:
        value = intent[key]
        if isinstance(value, dict):
            print(margin2 + key + ': ', end = '')
            traverse(value, inner, depth + 1, color, True)
        elif isinstance(value, list):
            print(margin2 + key + ': [')
            for p in value:
                traverse(p, inner, depth + 2, color)
            print(margin2 + ']')
        elif isinstance(value, str):
            print(margin2 + key + ':', '"' + value + '"')
        else:
            print(margin2 + key + ':', value)
    print(margin + '}')


@Agent('Log')
class LogAgent:

    @Any()
    @Raw()
    def x(self, intent):
        inner, _ = IntentTools.inner_intent(intent)
        traverse(intent, inner)
        print()
