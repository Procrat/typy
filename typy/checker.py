import ast
from logging import debug

from typy import insuline, namespace, nodes, builtin


def check(file_):
    type_map = namespace.build_type_map()
    builtin.add_to_type_map(type_map)

    module = ast.parse(file_.read())
    debug(ast.dump(module))
    insuline.replace_syntactic_sugar(module)
    debug(ast.dump(module))

    module = nodes.convert(type_map, module)

    module.check()
