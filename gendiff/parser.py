import json
import os
# import yaml


def parser(path):
    file_extension = os.path.splitext(path)[-1]
    if file_extension == '.json':
        data = json.load(open(path))
    # elif file_extension == '.yml' or file_extension == '.yaml':
    #     with open(path, 'r') as file:
    #         data = yaml.safe_load(file)
    else:
        return 'Inputed format is not supported'
    return data
