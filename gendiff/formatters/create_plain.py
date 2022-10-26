import json


def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    else:
        return json.dumps(value).replace('"', "'")


def create_plain(lst, path=""):
    result = []
    start = "Property '"
    for key in lst:
        key_name = key["key"]
        key_stat = key["status"]
        key_value = key["value"]
        current_path = path + f'.{key_name}' if path else key_name
        if key_stat == 'nested':
            result.append(create_plain(key_value, current_path))
        elif key_stat == 'changed':
            result.append(
                f"{start}{current_path}' was updated. "
                f"From {to_str(key_value['old_value'])} "
                f"to {to_str(key_value['new_value'])}")
        elif key_stat == 'deleted':
            result.append(
                f"{start}{current_path}' was removed"
            )
        elif key_stat == 'added':
            result.append(
                f"{start}{current_path}' was added with value: "
                f"{to_str(key_value)}"
            )
    return '\n'.join(result)
