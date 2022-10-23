def to_str(value):
    vals = ['true', 'false', 'null']
    if isinstance(value, dict):
        return "[complex value]"
    elif value in vals:
        return value
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


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
