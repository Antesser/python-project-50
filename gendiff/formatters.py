import json


def prettify(dictionary):
    statuses = ('changed', 'added', 'deleted', 'unchanged', 'changeddict')
    diff = '{\n'
    for i in dictionary.items():
        print(i)
        value = i[1][1]
        if i[1][0] not in statuses:
            diff += f'{i[0]}: {i[1]}\n'
            return diff + '}'
        if i[1][0] == 'changed':
            diff += f'- {i[0]}: {i[1][1]}\n'
            diff += f'+ {i[0]}: {i[1][2]}\n'
        if i[1][0] == 'added':
            diff += f'+ {i[0]}: {value}\n'
        if i[1][0] == 'deleted':
            diff += f'- {i[0]}: {value}\n'
        if i[1][0] == 'unchanged' or i[1][0] == 'changeddict':
            diff += f'  {i[0]}: {value}\n'
    return diff + '}'


def create_json(file):
    diff = json.dumps(file)
    return diff


def create_plain(dic, addon='', line=''):
    start = "Property '" + addon
    ldic = list(dic)
    for key in ldic:
        value = dic.get(key)
        if value[0] == 'deleted':
            line += f"{start}{key}' was removed\n"
        if value[0] == 'added':
            if isinstance(value[1], dict):
                finish = "'complex value'"
            else:
                finish = f"'{value[1]}'"
            line += f"{start}{key}' was added with value: {finish}\n"
        if value[0] == 'changeddict':
            if isinstance(value[-1], dict):
                line = create_plain(value[-1], key + '.', line)
            else:
                line += f"{start}{key}' was changed from '{value[1]}' to"
                f"{value[2]}'\n"
    return line
