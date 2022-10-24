import json


def check_complex(value):
    if isinstance(value, dict):
        return "[complex value]"
    else:
        return json.dumps(value)


def check_path(path, key_name):
    return path + f'.{key_name}' if path else key_name


def create_plain(lst, path=""):
    result = []
    start = "Property '"
    for key in lst:
        current_path = check_path(path, key['key'])
        key_stat = key["status"]
        key_value = key["value"]
        if key_stat == 'changeddict':
            result.append(create_plain(key_value, current_path))
        elif key_stat == 'changed':
            result.append(
                f"{start}{current_path}' was updated. "
                f"From {check_complex(key_value['old_value'])} "
                f"to {check_complex(key_value['new_value'])}")
        elif key_stat == 'deleted':
            result.append(
                f"{start}{current_path}' was removed"
            )
        elif key_stat == 'added':
            result.append(
                f"{start}{current_path}' was added with value: "
                f"{check_complex(key_value)}"
            )
    return '\n'.join(result)
