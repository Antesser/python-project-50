SPACES = '   '


def prettify_val(value, lvl):
    return [value['status'], value['key'], value['value']]


def prettify(lst, lvl=1):
    diff = ''
    for key in lst:
        if isinstance(key['value'], list):
            value = prettify(key['value'], lvl)
        try:
            if isinstance(key['value'], dict):
                value = prettify(key['value'], lvl)
        except TypeError:
            value = prettify_val(key, lvl)
        else:
            value = prettify_val(key, lvl)
        indent = SPACES * lvl
        if value[0] == 'changed':
            diff += f"{indent}- {value[1]}: {value[2]['old_value']}\n"
            diff += f"{indent}+ {value[1]}: {value[2]['new_value']}\n"
        elif value[0] == 'added':
            diff += f"{indent}+ {value[1]}: {value[2]}\n"
        elif value[0] == 'deleted':
            diff += f"{indent}- {value[1]}: {value[2]}\n"
        elif value[0] == 'unchanged':
            diff += f"{indent}  {value[1]}: {value[2]}\n"
        elif value[0] == 'changeddict':
            diff += f"  {indent}{value[1]}:{prettify(value[2], lvl+1)}\n"
    return '{\n' + diff + indent + '}'


def create_plain(lst, addon='', line=''):
    start = "Property '" + addon
    for key in lst:
        if key['status'] == 'deleted':
            line += f"{start}{key['key']}' was removed\n"
        if key['status'] == 'added':
            if isinstance(key['value'], dict):
                finish = "[complex value]"
            else:
                finish = f"'{key['value']}'"
            line += f"{start}{key['key']}' was added with value: {finish}\n"
        if key['status'] == 'changeddict':
            line = create_plain(key['value'], addon + key['key'] + '.', line)
        elif key['status'] == 'changed':
            if isinstance(key['value']['old_value'], dict):
                finish_old = "[complex value]"
            else:
                finish_old = key['value']['old_value']
            if isinstance(key['value']['new_value'], dict):
                finish_new = "[complex value]"
            else:
                finish_new = key['value']['new_value']
            line += f"{start}{key['key']}' was updated. "\
                f"From '{finish_old}' to '{finish_new}'\n"
    return line
