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
