import json

SPACES = '    '


def lower(value):
    low = [True, False]
    if value in low:
        return str(value).lower()
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


def get_val(value, lvl):
    if isinstance(value, dict):
        return prettify_val(value, lvl)
    return value


def prettify_val(value, lvl):
    diff = ['{']
    for key, value in value.items():
        value = get_val(value, lvl=lvl+1)
        diff.append(
            f"{SPACES * (lvl + 2)}{key}: {value}"
        )
    diff.append(f"{SPACES * (lvl + 1)}}}")
    return '\n'.join(diff)


def prettify(lst, lvl=0):
    diff = []
    indent = SPACES * lvl
    for key in lst:
        key_name = key['key']
        key_stat = key['status']
        key_value = key['value']
        if key_stat == 'changeddict':
            diff.extend([
                f"{indent}    {key_name}: {{",
                prettify(key_value, lvl=lvl + 1),
                f"{indent}    }}"
            ])
        elif key_stat == 'changed':
            diff.extend([
                f"{indent}  - {key_name}: "
                f"{get_val(key['value']['old_value'], lvl)}",
                f"{indent}  + {key_name}: "
                f"{get_val(key['value']['new_value'], lvl)}"
            ])
        elif key_stat == 'added':
            diff.append(
                f"{indent}  + {key_name}: {get_val(key_value, lvl)}"
            )
        elif key_stat == 'deleted':
            diff.append(
                f"{indent}  - {key_name}: {get_val(key_value, lvl)}"
            )
        elif key_stat == 'unchanged':
            diff.append(
                f"{indent}    {key_name}: {get_val(key_value, lvl)}"
            )
    if not lvl:
        diff = ['{'] + diff + ['}']
    return '\n'.join(diff)


def is_complex(value):
    if isinstance(value, dict):
        return "[complex value]"
    else:
        return value


def create_plain(lst, addon='', line=''):
    start = "Property '" + addon
    for key in lst:
        key_name = key['key']
        key_stat = key['status']
        key_value = key['value']
        if key_stat == 'deleted':
            line += f"{start}{key_name}' was removed\n"
        if key_stat == 'added':
            finish = is_complex(key_value)
            line += f"{start}{key_name}' was added with value: {finish}\n"
        if key_stat == 'changeddict':
            line = create_plain(key_value, addon + key_name + '.', line)
        elif key_stat == 'changed':
            finish_old = is_complex(key_value['old_value'])
            finish_new = is_complex(key_value['new_value'])
            line += f"{start}{key_name}' was updated. "\
                f"From '{finish_old}' to '{finish_new}'\n"
    return line


def create_json(result):
    diff = json.dumps(result)
    return diff
