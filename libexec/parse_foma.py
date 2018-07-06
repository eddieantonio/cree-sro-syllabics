#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright (C) 2018 Eddie Antonio Santos <easantos@ualberta.ca>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gzip
from collections import namedtuple

# GLOBAL: sigma: (num, symbol) pairs.
sigma = []
states = []


class Symbol:
    def __repr__(self) -> str:
        return type(self).__name__


Epsilon = type('Epsilon', Symbol.__mro__, {})()
Unknown = type('Unknown', Symbol.__mro__, {})()
Identity = type('Identity', Symbol.__mro__, {})()


class InvalidState(ValueError):
    """
    Raised when parsing got in an invalid state.
    """


class State:
    def __init__(self, state_no, is_final_state, transitions=None):
        self.state_no = state_no
        self.is_final_state = is_final_state
        self.transitions = [] if transitions is None else transitions

    def append_transition(self, in_, out, target):
        self.transitions.append(
            Transition(in_, out, target)
        )

    def __repr__(self):
        return '{}(state_no={}, is_final_state={}, transitions={})'.format(
            type(self).__name__,
            self.state_no, self.is_final_state,
            self.transitions
        )


class Transition(namedtuple('_Transition', 'in_ out target')):
    """
    Signifies a transition from one state to another.
    """


def read_header(line):
    assert line == '##foma-net 1.0##'
    return read_props_start


def read_props_start(line):
    assert line == '##props##'
    return read_props


def read_props(line):
    """
    Read the properties, that I'm just going to completely ignore for now.
    """
    (
        _arity, _arc_count, _state_count, _line_count, _final_count,
        _path_count, is_deterministic, _is_pruned, _is_minimized,
        is_epsilon_free,
        _is_loop_free, _extras, *_name
    ) = line.split()
    assert is_deterministic == '1', 'network must be deterministic'
    assert is_epsilon_free == '1', 'network must not have epsilon transitions'
    return read_sigma_start


def read_sigma_start(line):
    assert line == '##sigma##', line
    return read_sigma_entry


def read_sigma_entry(line):
    global sigma
    if line == '##states##':
        return read_state_array

    num_str, _, symbol_str = line.partition(' ')
    sigma.append((int(num_str), to_symbol(symbol_str)))
    return read_sigma_entry


def is_sentinel_state(nums):
    return all(n == -1 for n in nums)


def read_state_array(nums):
    nums = [int(c) for c in line.split()]
    if is_sentinel_state(nums):
        return read_end
    elif len(nums) == 5:
        # New state
        state_no, in_, out, target, final_state = nums
        states.append(State(state_no, bool(final_state)))
    elif len(nums) == 4:
        # New state
        state_no, in_, target, final_state = nums
        out = in_
        states.append(State(state_no, bool(final_state)))
    elif len(nums) == 3:
        # Old state
        in_, out, target = nums
    elif len(nums) == 2:
        # Old state
        in_, target = nums
        out = in_
    else:
        raise InvalidState

    states[-1].append_transition(in_, out, target)
    return read_state_array


def read_end(line):
    assert line == '##end##'
    return invalid_state


def invalid_state(line):
    """
    Should never reach this state.
    """
    raise ValueError(line)


def to_symbol(text):
    if text == '@_EPSILON_SYMBOL_@':
        return Epsilon
    elif text == '@_UNKNOWN_SYMBOL_@':
        return Unknown
    elif text == '@_IDENTITY_SYMBOL_@':
        return Identity
    else:
        assert len(text) == 1
        return text


if __name__ == '__main__':
    import sys
    from pprint import pprint

    _, filename = sys.argv

    with gzip.open(filename, 'rt', encoding='UTF-8') as fsm_file:
        next_state = read_header
        for line in fsm_file:
            next_state = next_state(line.rstrip())

    print('SIGMA = ', end='')
    pprint(sigma)
    print('STATES = ', end='')
    pprint(states)
