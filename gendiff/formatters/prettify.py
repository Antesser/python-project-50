import json


SPACES = '    '
STATUSES = {'added': '  + ',
            'deleted': '  - ',
            'unchanged': '    '}


def to_str(value, lvl):
    if isinstance(value, dict):
        if isinstance(value, dict):
            diff = '{\n'
            for key, value in value.items():
                diff += f'{SPACES * (lvl + 2)}{key}: '
                diff += prettify_val(value, lvl=lvl + 1) + '\n'
            diff += SPACES * (lvl) + '    }'
        else:
            diff = str(value)
        return diff
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
                f"{to_str(key_value['old_value'], lvl)}",
                f"{indent}  + {key_name}: "
                f"{to_str(key_value['new_value'], lvl)}"
            ])
        else:
            status = STATUSES.get(key_stat)
            diff.append(
                f"{indent}{status}{key_name}: {to_str(key_value, lvl)}"
            )
    if not lvl:
        diff = ['{'] + diff + ['}']
    return '\n'.join(diff)
