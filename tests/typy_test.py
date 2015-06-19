"""
The `test_files` folder contains pairs of files (xxx.py, xxx.out).
This module checks whether typy run on xxx.py returns the same as xxx.out.
"""

import pytest
import typy.checker
import typy.exceptions
import os.path

HERE = os.path.join(os.path.dirname(__file__), 'test_files')
TEST_FILES = [
    'assignment',
    'builtin_attribute_set',
    # 'builtin_types',
    'closure',
    'constants',
    'ifexp',
    # 'magic_methods',
    'test1',
    'test2',
    # 'test3',
    # 'test4',
]


@pytest.mark.parametrize("test_filename", TEST_FILES)
def test_feature(test_filename):
    with open(os.path.join(HERE, test_filename + '.py')) as test_file:
        try:
            typy.checker.check(test_file)
            out = 'no errors'
        except typy.exceptions.CheckError as error:
            out = error.msg

    with open(os.path.join(HERE, test_filename + '.out')) as expected_out_file:
        expected_out = expected_out_file.read().strip()

    assert out == expected_out
