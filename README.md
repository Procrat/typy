# typy
A static type checker for Python 3 (using control flow analysis).

## WORK IN PROGRESS
This isn't even remotely finished as a practically useful type checker. This
project originated as a proof of concept and is currently still in this state.

## WARNING
Even if all Python language features were supported, it is not possible to have
a type checker that always works. This is due to the dynamic nature of Python.
For example, classes and functions can be created, deleted and otherwise
manipulated on the fly. Don't expect magic from typy.

## Usage
Install `typy` by running `python setup.py install`.

Run `typy <file>` to type check a file.

Run `typy -v <file>` for debugging output.

## Tests
All tests can be run with `py.test`.

Install `pytest` if need be: `pip install pytest`

## (Somewhat) supported features
- Function/method parameter type checking
- Function/method return type checking
- Replacement of builtin operators to magic method calls
  - numeric operators
  - bit operators
  - comparison operators
- Handled expressions: attributes, calls, builtin function calls, names,
  comparisons, comparison chaining, name constants, control flow statements
- Handled statements: function definitions, return, class definitions,
  assignments
- Handling of closures
- Checking a limited set builtin types and their attributes (integers, booleans, tuples)
- Checking whether a name gets bound to different types

## Will soon be supported
- All attributes of all builtin types
- Sequence types (TODO implement get_enclosed_type and is_iterable)
- Statements: imports (Import, ImportFrom)
    - Needed for: module namespace/attributes
- Intersection types
    - Needed for: boolean operators, if-expression, comparisons In & NotIn
- Recursive functions
- Optional and keyword arguments
    - Needed for: a lot of builtin functions
- Replacement of some builtin functions to magic methods (len, next, iter ...)
- Comparison operators: Is, IsNot
- Global/built-in functions

## Not supported (yet)
- Inheritance
- Default arguments
- Varargs
- Keyword arguments
- Line number mentioning for errors
- Checking of function definitions which are not explicitly called
- Expressions:
  - Ellipses (Ellipsis)
  - Generator expressions (GeneratorExp)
  - Lambdas (Lambda)
  - Starred expression (Starred)
  - Yield (Yield, YieldFrom)
  - Comprehensions (ListComp, DictComp, SetComp)
- Statements:
  - Asserts (Assert)
  - Deletes (Delete)
  - Contexts (With)
  - Augmented assigns (AugAssign)
  - Global and nonlocal statements (Global, Nonlocal)
  - Exception (Try, Raise, ExceptHandler)
- Expressions contexts: AugLoad, AugStore, Del, Param
- Subscripting (with handling of slices: ExtSlice, Index, Slice)
- Constant folding
- Descriptor protocol
- getattr / hasattr / setattr
- Decorators
- A lot of magic methods
- Other uncommon dynamic Python magic

## Acknowledgements
A big thanks goes out to the PyPy compiler and the CPython compiler for
supplying the exact semantics of some Python concepts.
