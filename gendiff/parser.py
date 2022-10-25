import json
import os
import yaml


def check_extension(path):
    file_extension = os.path.splitext(path)[-1]
    return file_loader(path, file_extension)


def file_loader(path, extension):
    if extension == '.json':
        data = json.load(open(path))
    elif extension == '.yml' or '.yaml':
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
    else:
        raise ValueError('Inputed format is not supported')
    return data


def parser(path):
    data = check_extension(path)
    return data
