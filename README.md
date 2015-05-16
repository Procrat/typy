# typy
A static type checker for Python

## WORK IN PROGRESS
This isn't even remotely finished and the code is still a mess.

## (Somewhat) supported type checking
- Function/method parameter type checking
- Function/method return type checking

## (Somewhat) supported handling of language features
- Builtin function: print
- Replacement of builtin operators to magic method calls
  - numeric operators
  - bit operators
  - comparison operators
- Expressions: attributes, calls, builtin function calls, names
- Statements: function definitions, return

## Will soon be supported
- Builtin functions except print
- Replacement of some builtin functions to magic methods (len, next, iter ...)
- Builtin types: Bytes, Dict, List, Num, Set, Str, Tuple
- Expressions: NameConstant, boolean operators (BoolOp, And, Or)
- Statements
  - class definitions (ClassDef)
  - assignments (Assign)
  - control flow statements (If, While, For, Break, Continue)
  - imports (Import, ImportFrom)
  - deletes (Delete)
  - contexts (With)
- Methods
- Inheritance
- Recursive functions
- Warning when builtin names get assigned (typy might fail)
- Subscripting (with handling of slices: ExtSlice, Index, Slice)
- Unary operator: Not
- Comparison operators (Is, IsNot, In, NotIn)

## Not supported (yet)
- Default arguments
- Keyword arguments
- Line number mentioning for error
- Checking of functions which are not explicitly called
- Comparison chaining
- Expressions:
  - Ellipses (Ellipsis)
  - Generator expressions (GeneratorExp)
  - Lambdas (Lambda)
  - Starred expression (Starred)
  - Yield (Yield, YieldFrom)
  - If-expression (IfExp)
  - Comprehensions (ListComp, DictComp, SetComp)
- Statements:
  - Asserts (Assert)
  - Augmented assigns (AugAssign)
  - Global and nonlocal statements (Global, Nonlocal)
  - Exception (Try, Raise, ExceptHandler)
- Expressions contexts (?): AugLoad, AugStore, Del, Param
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
