from gendiff.formatters.create_json import create_json
from gendiff.formatters.create_plain import create_plain
from gendiff.formatters.prettify import prettify
from gendiff.parser import find_extension, load_file, parser
from gendiff.create_diff import create_diff


def generate_diff(first_file, second_file, format='stylish'):
    first = parser(load_file(first_file), find_extension(first_file))
    second = parser(load_file(second_file), find_extension(second_file))
    diff = create_diff(first, second)
    file = formatting_diff(diff, format)
    return file


def formatting_diff(diff, format):

    if format == 'stylish':
        diff = prettify(diff)
    elif format == 'plain':
        diff = create_plain(diff)
    elif format == 'json':
        diff = create_json(diff)
    else:
        raise ValueError('Inputed format is not supported')
    return diff
