import json
import os
import yaml


def file_reader(file):
    return os.path.splitext(file)[-1]


def parser(path):
    if file_reader(path) == '.json':
        data = json.load(open(path))
    elif file_reader(path) == '.yml' or '.yaml':
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
    else:
        raise ValueError('Inputed format is not supported')
    return data
