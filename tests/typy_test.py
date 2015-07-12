"""
The `test_files` folder contains pairs of files (xxx.py, xxx.out).
This module checks whether typy run on xxx.py returns the same as xxx.out.
"""

import os.path
import pytest
import typy.checker
import typy.exceptions

HERE = os.path.join(os.path.dirname(__file__), 'test_files')
TEST_FILES = [
    'assignment',
    'attributes',
    'base_types',
    'builtin_attribute_set',
    'closure',
    'constants',
    'comparisons',
    'first_class_class',
    'first_class_class_bad',
    'ifexp',
    'method',
    'non_existent_name',
    'non_callable',
    'return_of_pass',
    'return_value',
    'static_function',
    'static_function_bad_call',
    'tuple',
    'wrong_argument_number',
    'wrong_builtin_parameter',
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
