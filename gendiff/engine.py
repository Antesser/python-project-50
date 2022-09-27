from gendiff.parser import parser
from gendiff.formatters import prettify, create_plain, create_json


def start_program(args):
    print(generate_diff(args.first_file, args.second_file, format='string'))


def generate_diff(first_file, second_file, format=''):
    first = parser(first_file)
    second = parser(second_file)
    result = check_diff(first, second)
    if format == 'plain':
        diff = create_plain(result)
    elif format == 'json':
        diff = create_json(result)
    else:
        diff = prettify(result)
    return diff


def check_diff(first, second):
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
                             check_diff(first_value, second_value)]
            else:
                diff[key] = ['changed', str(first_value), str(second_value)]
        else:
            diff[key] = ['unchanged', str(first_value)]
    sorted_tuple = sorted(diff.items(), key=lambda x: x[0])
    return dict(sorted_tuple)
