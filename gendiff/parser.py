import json
import os
import yaml


def check_extension(path):
    return os.path.splitext(path)[-1]


def file_loader(path):
    with open(path) as file:
        return file.read()


def parser(path, extension):
    if extension == 'json':
        return json.loads(path)
    elif extension == 'yaml' or 'yml':
        return yaml.safe_load(path)
