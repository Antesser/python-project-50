import json
import os
import yaml


def file_loader(path):
    file_extension = os.path.splitext(path)[-1]
    if file_extension == '.json':
        data = json.load(open(path))
    elif file_extension == '.yml' or '.yaml':
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
    else:
        raise ValueError('Inputed format is not supported')
    return data


def parser(path):
    data = file_loader(path)
    return data
