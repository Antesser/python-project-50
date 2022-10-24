import json


SPACES = '    '


def from_json(data):
    for value in data:
        if isinstance(value, dict):
            from_json(value)
        else:
            return json.dumps(value)


def get_val(value, lvl):
    if isinstance(value, dict):
        return prettify_val(value, lvl)
    return json.dumps(value).replace('"', '')


def prettify_val(value, lvl):
    if isinstance(value, dict):
        diff = '{\n'
        for key, value in value.items():
            diff += f'{SPACES * (lvl + 2)}{key}: '
            diff += prettify_val(value, lvl=lvl + 1) + '\n'
        diff += SPACES * (lvl) + '    }'
    else:
        diff = str(value)
    return diff


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
                f"{get_val(key_value['old_value'], lvl)}",
                f"{indent}  + {key_name}: "
                f"{get_val(key_value['new_value'], lvl)}"
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
