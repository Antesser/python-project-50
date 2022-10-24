from gendiff.formatters.create_json import create_json
from gendiff.formatters.create_plain import create_plain
from gendiff.formatters.prettify import prettify
from gendiff.parser import parser
from gendiff.create_diff import create_diff


def generate_diff(first_file, second_file, format=''):
    first = parser(first_file)
    second = parser(second_file)
    diff = create_diff(first, second)
    if format == 'plain':
        diff = create_plain(diff)
    elif format == 'json':
        diff = create_json(diff)
    else:
        diff = prettify(diff)
    return diff
