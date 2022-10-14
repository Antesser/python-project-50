from gendiff.formatters import create_json, create_plain, prettify
from gendiff.parser import parser


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


def lower(value):
    low = ['True', 'False']
    if str(value) in low:
        return value.lower()
    else:
        return value


def check_diff(first, second):
    diff = []
    keys_first = first.keys()
    keys_second = second.keys()
    keys_both = keys_second & keys_first
    for key in keys_both:
        first_value = first.get(key)
        second_value = second.get(key)
        f_val = lower(first_value)
        s_val = lower(second_value)
        if f_val != s_val:
            if isinstance(f_val, dict) and isinstance(s_val, dict):
                diff_chd = ({'key': key, 'status': 'changeddict',
                            'value': check_diff(f_val, s_val)})
                diff.append(diff_chd)
            else:
                diff_changed = ({'key': key, 'status': 'changed',
                                 'value': {
                                        'old_value': f_val,
                                        'new_value': s_val}
                                 })
                diff.append(diff_changed)
        else:
            diff_unchanged = ({'key': key, 'status': 'unchanged',
                               'value': first_value})
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
