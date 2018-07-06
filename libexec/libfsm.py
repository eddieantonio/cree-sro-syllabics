#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

from collections import namedtuple


class Symbol:
    """
    Represents a non-character symbol.
    """
    def __repr__(self) -> str:
        return type(self).__name__


Epsilon = type('Epsilon', Symbol.__mro__, {})()
Unknown = type('Unknown', Symbol.__mro__, {})()
Identity = type('Identity', Symbol.__mro__, {})()


class State:
    def __init__(self, state_no, is_final_state, transitions=None):
        self.state_no = state_no
        self.is_final_state = is_final_state
        self.transitions = [] if transitions is None else transitions

    def append_transition(self, in_, out, target):
        self.transitions.append(
            Transition(upper=in_, lower=out, target=target)
        )

    def __repr__(self):
        return '{}(state_no={}, is_final_state={}, transitions={})'.format(
            type(self).__name__,
            self.state_no, self.is_final_state,
            self.transitions
        )


class Transition(namedtuple('_Transition', 'upper lower target')):
    """
    Signifies a transition from one state to another.
    """
    def __str__(self):
        return '<{}:{} (-> {})>'.format(
            self.upper, self.lower, self.target
        )
