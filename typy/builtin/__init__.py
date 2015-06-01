from typy.builtin import data_types, functions


def add_to_type_map(type_map):
    data_types.add_to_type_map(type_map)
    functions.add_to_type_map(type_map)
