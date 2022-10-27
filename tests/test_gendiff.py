from gendiff.engine import generate_diff
import pytest
from tests import answer


@pytest.mark.parametrize("first_file, second_file, result, format", [
    (
        './tests/fixtures/first.yaml',
        './tests/fixtures/second.yaml',
        answer.YAML,
        'stylish'
    ),
    (
        './tests/fixtures/first.json',
        './tests/fixtures/second.json',
        answer.YAML,
        'stylish'
    ),
    (
        './tests/fixtures/first_nested.yaml',
        './tests/fixtures/second_nested.yaml',
        answer.NESTED,
        'stylish'
    ),
    (
        './tests/fixtures/first_nested.json',
        './tests/fixtures/second_nested.json',
        answer.NESTED,
        'stylish'
    ),
    (
        './tests/fixtures/first_nested.yaml',
        './tests/fixtures/second_nested.yaml',
        answer.PLAIN,
        'plain'
    ),
    (
        './tests/fixtures/first_nested.json',
        './tests/fixtures/second_nested.json',
        answer.PLAIN,
        'plain'
    ),
    (
        './tests/fixtures/first_nested.yaml',
        './tests/fixtures/second_nested.yaml',
        answer.NESTED_JSON,
        'json'
    ),
    (
        './tests/fixtures/first_nested.json',
        './tests/fixtures/second_nested.json',
        answer.NESTED_JSON,
        'json'
    ),
])
def test_gendiff(first_file, second_file, result, format):
    assert generate_diff(first_file, second_file, format) == result
