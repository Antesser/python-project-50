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
            fst_value = first.get(key)
            scd_value = second.get(key)
            if fst_value != scd_value:
                if isinstance(fst_value, dict) and isinstance(scd_value, dict):
                    diff_chd = ({'key': key, 'status': 'changeddict',
                                'value': create_diff(fst_value, scd_value)})
                    diff.append(diff_chd)
                else:
                    diff_changed = ({'key': key, 'status': 'changed',
                                    'value': {'old_value': fst_value,
                                              'new_value': scd_value}})
                    diff.append(diff_changed)
            else:
                diff_unchanged = ({'key': key, 'status': 'unchanged',
                                   'value': fst_value})
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
