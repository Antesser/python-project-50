import json


def generate_diff(file1, file2):
    first = json.load(open(file1))
    second = json.load(open(file2))
    common = first.keys() & second.keys()
    only_before = first.keys() - second.keys()
    only_after = second.keys() - first.keys()
    result = ['{', ]
    for i in common:
        if first[i] == second[i]:
            result.append('   ' + i + ': ' + str(first[i]))
        else:
            result.append(' + ' + i + ': ' + str(second[i]))
            result.append(' - ' + i + ': ' + str(first[i]))
    for i in only_before:
        result.append(' - ' + i + ': ' + str(first[i]))
    for i in only_after:
        result.append(' + ' + i + ' ' + str(second[i]))
    result.append('}')
    answer = ''
    for i in result:
        answer = answer + i + '\n'
    return answer
