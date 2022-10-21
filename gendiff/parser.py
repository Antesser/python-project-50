import json
import os
import yaml


def parser(path):
    file_extension = os.path.splitext(path)[-1]
    if file_extension == '.json':
        data = json.load(open(path))
    elif file_extension == '.yml' or file_extension == '.yaml':
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
    else:
        return 'Inputed format is not supported'
    lower(data)
    return data


def lower(data):
    for key, item in data.items():
        if isinstance(item, dict):
            lower(item)
        if item is True:
            data[key] = 'true'
        elif item is False:
            data[key] = 'false'
        elif isinstance(item, type(None)):
            data[key] = 'null'
