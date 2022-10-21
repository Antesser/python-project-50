from gendiff.formatters import create_json, create_plain, prettify
from gendiff.parser import parser


def start_program(args):
    print(generate_diff(args.first_file, args.second_file, args.format))


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
    diff = []
    keys_first = first.keys()
    keys_second = second.keys()
    keys_both = keys_second & keys_first
    for key in keys_both:
        fst_value = first.get(key)
        scd_value = second.get(key)
        if fst_value != scd_value:
            if isinstance(fst_value, dict) and isinstance(scd_value, dict):
                diff_chd = ({'key': key, 'status': 'changeddict',
                            'value': check_diff(fst_value, scd_value)})
                diff.append(diff_chd)
            else:
                diff_changed = ({'key': key, 'status': 'changed',
                                 'value': {'old_value': fst_value,
                                           'new_value': scd_value}})
                diff.append(diff_changed)
        else:
            diff_unchanged = ({'key': key, 'status': 'unchanged',
                              'value': fst_value})
            diff.append(diff_unchanged)
    deleted = keys_first - keys_second
    for key in deleted:
        diff_del = {'key': key, 'status': 'deleted', 'value': first.get(key)}
        diff.append(diff_del)
    added = keys_second - keys_first
    for key in added:
        diff_add = {'key': key, 'status': 'added', 'value': second.get(key)}
        diff.append(diff_add)
    diff.sort(key=lambda diff: diff['key'])
    return diff
