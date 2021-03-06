#!/usr/bin/env python
"""Tests for color proximity"""
from ColorProximity import ColorProximity

CP = ColorProximity()

# test as tuples
assert str(CP.proximity((255, 255, 255), (255, 255, 254))) == \
    str(0.507421915175), 'Fail, test 1'
assert str(CP.proximity((255, 255, 255), (255, 255, 255))) == str(0.0), \
    'Fail, test 2'
assert str(CP.proximity((255, 255, 255), (0, 0, 0))) == str(100.000000625), \
    'Fail, test 3'
assert str(CP.proximity((255, 255, 255), (1, 1, 1))) == str(99.7260006267), \
    'Fail, test 4'

# test as list
assert str(CP.proximity([255, 255, 255], [255, 255, 254])) == \
    str(0.507421915175), 'Fail, test 5'
assert str(CP.proximity([255, 255, 255], [255, 255, 255])) == str(0.0), \
    'Fail, test 6'
assert str(CP.proximity([255, 255, 255], [0, 0, 0])) == str(100.000000625), \
    'Fail, test 7'
assert str(CP.proximity([255, 255, 255], [1, 1, 1])) == str(99.7260006267), \
    'Fail, test 8'

# tuple w/alpha value
assert str(CP.proximity((255, 255, 255, 20), (255, 255, 254, 30))) == \
    str(0.507421915175), 'Fail, test 9'

# list w/alpha value
assert str(CP.proximity([255, 255, 255, 20], [255, 255, 254, 30])) == \
    str(0.507421915175), 'Fail, test 10'

# mixed tuple and list w/alpha value
assert str(CP.proximity([255, 255, 255, 20], (255, 255, 254, 30))) == \
    str(0.507421915175), 'Fail, test 11'

print 'pass'
