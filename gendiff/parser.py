import json
import os
import yaml


def file_reader(file):
    return os.path.splitext(file)[-1]


def parser(path):
    file_extension = file_reader(path)
    if file_extension == '.json':
        data = json.load(open(path))
    elif file_extension == '.yml' or file_extension == '.yaml':
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
    else:
        raise ValueError('Inputed format is not supported')
    return data
