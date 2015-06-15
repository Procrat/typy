# typy
A static type checker for Python 3 (using control flow analysis).

## WORK IN PROGRESS
This isn't even remotely finished. This project originated as a proof of
concept and is currently still in this state.

## WARNING
Even if all Python language features were supported, it is not possible to have
a type checker that always works. This is due to the dynamic nature of Python.
For example, classes and functions can be created, deleted and otherwise
manipulated on the fly. Don't expect magic from typy.

## Usage
Install `typy` by running `python setup.py install`.
Run `typy <file>` to type check a file.

## Tests
All tests can be run with `py.test`.
Install `pytest` if need be: `pip install pytest`

## (Somewhat) supported handling of language features
- Function/method parameter type checking
- Function/method return type checking
- Replacement of builtin operators to magic method calls
  - numeric operators
  - bit operators
  - comparison operators
- Expressions: attributes, calls, builtin function calls, names, comparison
  chaining, name constants, control flow statements
- Statements: function definitions, return, class definitions, assignments
- Closures

## Will soon be supported
- All attributes of all builtin types
    - istypeof for all builtins + klassen
- Sequence types (implement get_enclosed_type/is_iterable)
- Statements: imports (Import, ImportFrom)
    - Module namespace/attributes
- Intersection types
    - for boolean operators, if-expression
- Recursive functions
- Optional and keyword arguments
    - needed for most builtin functions
- Replacement of some builtin functions to magic methods (len, next, iter ...)
- Comparison operators (Is, IsNot, In, NotIn)
- First class functions / classes

## Not supported (yet)
- Inheritance
- Default arguments
- Keyword arguments
- Line number mentioning for errors
- Checking of function definition which are not explicitly called
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
- Expressions contexts (?): AugLoad, AugStore, Del, Param
- Subscripting (with handling of slices: ExtSlice, Index, Slice)
- Constant folding
- Descriptor protocol
- getattr/hasattr/setattr
- Uncommon dynamic Python magic
- Magic methods:
  - right side ops (__radd__ __rsub__ __rmul__ __rtruediv__ __rmod__ __rpow__
    __rlshift__ __rrshift__ __ror__ __rxor__ __rand__ __rfloordiv__
    __rdivmod__)
  - __abs__
  - __reduce_ex__
  - __format__
  - __repr__
  - __setattr__
  - __sizeof__
  - __bool__
  - __getattribute__
  - __str__
  - __ceil__
  - __getnewargs__
  - __neg__
  - __class__
  - __new__
  - __subclasshook__
  - __delattr__
  - __hash__
  - __dir__
  - __index__
  - __pos__
  - __round__
  - __trunc__
  - __divmod__
  - __init__
  - __doc__
  - __int__
  - __float__
  - __floor__
  - __reduce__

## Acknowledgements
A big thanks goes out to the PyPy compiler and the CPython compiler for
supplying the exact semantics of some Python concepts.
