SPACES = '  '


def prettify(lst, lvl=0):
    diff = ''
    for key in lst:
        if isinstance(key['value'], list):
            value = prettify(key['value'], lvl+1)
        try:
            if isinstance(key['value'], dict):
                value = prettify(key['value'], lvl+1)
        except TypeError:
            value = key['value']
        else:
            value = key['value']
        diff += SPACES * lvl
        if key['status'] == 'changed':
            diff += f"- {key['key']}: {key['value']['old_value']}\n"
            diff += SPACES * lvl
            diff += f"+ {key['key']}: {key['value']['new_value']}\n"
        if key['status'] == 'added':
            diff += f"+ {key['key']}: {value}\n"
        if key['status'] == 'deleted':
            diff += f"- {key['key']}: {value}\n"
        if key['status'] == 'unchanged':
            diff += f"  {key['key']}: {value}\n"
        if key['status'] == 'changeddict':
            diff += f"{key['key']}: {'{'}{value}\n"
    diff = diff.replace('{{', '{')
    return '{\n' + diff + '}'


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
