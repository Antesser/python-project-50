from gendiff.engine import generate_diff
import pytest


@pytest.mark.parametrize("first_file, second_file, result, format", [
    (
        './tests/fixtures/first.json',
        './tests/fixtures/second.json',
        './tests/fixtures/answer_j.y.txt',
        'stylish'
    ),
    (
        './tests/fixtures/first.yaml',
        './tests/fixtures/second.yaml',
        './tests/fixtures/answer_j.y.txt',
        'stylish'
    ),
    (
        './tests/fixtures/first_nested.json',
        './tests/fixtures/second_nested.json',
        './tests/fixtures/answer_nested.txt',
        'stylish'
    ),
    (
        './tests/fixtures/first_nested.json',
        './tests/fixtures/second_nested.json',
        './tests/fixtures/answer_plain.txt',
        'plain'
    ),
])
def test_gendiff(first_file, second_file, result, format):
    assert generate_diff(first_file, second_file, format) == result
