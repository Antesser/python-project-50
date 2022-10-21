import json

SPACES = '    '


def get_val(value, lvl):
    if isinstance(value, dict):
        return prettify_val(value, lvl)
    return value


def prettify_val(value, lvl):
    diff = ['{']
    for key, value in value.items():
        value = get_val(value, lvl=lvl + 1)
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
        else:
            status = other_statuses(key_stat)
            diff.append(
                f"{indent}{status}{key_name}: {get_val(key_value, lvl)}"
            )
    if not lvl:
        diff = ['{'] + diff + ['}']
    return '\n'.join(diff)


def other_statuses(key_stat):
    statuses = {'added': '  + ', 'deleted': '  - ', 'unchanged': '    '}
    return statuses.get(key_stat)


def is_complex(value):
    vals = ['true', 'false', 'null']
    if isinstance(value, dict):
        return "[complex value]"
    elif value in vals:
        return value
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def check_addon(addon, key_name):
    return addon + f'.{key_name}' if addon else key_name


def create_plain(lst, addon=""):
    result = []
    start = "Property '"
    for key in lst:
        current_addon = check_addon(addon, key['key'])
        key_stat = key["status"]
        key_value = key["value"]
        if key_stat == 'changeddict':
            result.append(create_plain(key_value, current_addon))
        elif key_stat == 'changed':
            result.append(
                f"{start}{current_addon}' was updated. "
                f"From {is_complex(key_value['old_value'])} "
                f"to {is_complex(key_value['new_value'])}")
        elif key_stat == 'deleted':
            result.append(
                f"{start}{current_addon}' was removed"
            )
        elif key_stat == 'added':
            result.append(
                f"{start}{current_addon}' was added with value: "
                f"{is_complex(key_value)}"
            )
    return '\n'.join(result)


def create_json(result):
    diff = json.dumps(result)
    return diff
