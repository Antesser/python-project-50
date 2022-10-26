def create_diff(first, second):
    diff = []
    keys_first = first.keys()
    keys_second = second.keys()
    keys_all = keys_second | keys_first
    keys_both = keys_second & keys_first
    deleted = keys_first - keys_second
    added = keys_second - keys_first
    for key in keys_all:
        if key in keys_both:
            first_value = first.get(key)
            second_value = second.get(key)
            if first_value != second_value:
                if isinstance(first_value, dict) and isinstance(second_value,
                                                                dict):
                    diff_nested = ({'key': key, 'status': 'nested',
                                    'value': create_diff(first_value,
                                                         second_value)})
                    diff.append(diff_nested)
                else:
                    diff_changed = ({'key': key, 'status': 'changed',
                                    'value': {'old_value': first_value,
                                              'new_value': second_value}})
                    diff.append(diff_changed)
            else:
                diff_unchanged = ({'key': key, 'status': 'unchanged',
                                   'value': first_value})
                diff.append(diff_unchanged)
        elif key in deleted:
            diff_del = {'key': key, 'status': 'deleted',
                        'value': first.get(key)}
            diff.append(diff_del)
        elif key in added:
            diff_add = {'key': key, 'status': 'added',
                        'value': second.get(key)}
            diff.append(diff_add)
    diff.sort(key=lambda diff: diff['key'])
    return diff
