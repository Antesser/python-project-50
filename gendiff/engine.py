from gendiff.parser import parser
from gendiff.formatters import prettify


def generate_diff(first_file, second_file):
    first = parser(first_file)
    second = parser(second_file)
    diff = {}
    keys_first = first.keys()
    keys_second = second.keys()
    deleted = keys_first - keys_second
    for key in deleted:
        diff[key] = ['deleted', first.get(key)]
    added = keys_second - keys_first
    for key in added:
        diff[key] = ['added', second.get(key)]
    keys_both = keys_second & keys_first
    for key in keys_both:
        first_value = first.get(key)
        second_value = second.get(key)
        if first_value != second_value:
            if isinstance(first_value, dict) and isinstance(second_value,
                                                            dict):
                diff[key] = ['changeddict',
                             generate_diff(first_value, second_value)]
            else:
                diff[key] = ['changed', first_value, second_value]
        else:
            diff[key] = ['unchanged', first_value]
    sorted_tuple = sorted(diff.items(), key=lambda x: x[0])
    a = prettify(dict(sorted_tuple))
    return a
