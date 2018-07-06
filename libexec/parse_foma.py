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

sigma = []


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
    # TODO: ...
    return read_sigma_start


def read_sigma_start(line):
    assert line == '##sigma##', line
    return read_sigma_entry


def read_sigma_entry(line):
    if line == '##states##':
        return read_state

    num_str, _, symbol_str = line.partition(' ')
    sigma.append((int(num_str), to_symbol(symbol_str)))
    return read_sigma_entry


def read_state(line):
    import pdb
    pdb.set_trace()


class Symbol:
    def __repr__(self) -> str:
        return type(self).__name__


Epsilon = type('Epsilon', Symbol.__mro__, {})()
Unknown = type('Unknown', Symbol.__mro__, {})()
Identity = type('Identity', Symbol.__mro__, {})()


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


with open('Cans-to-Latn.txt') as fsm_file:
    next_state = read_header
    for line in fsm_file:
        next_state = next_state(line.rstrip())
