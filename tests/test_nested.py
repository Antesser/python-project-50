from gendiff.engine import generate_diff


def test_nested():
    a = './tests/fixtures/answer_nested.json'
    b = generate_diff(
        './tests/fixtures/first_nested.json',
        './tests/fixtures/second_nested.json',
        'string'
    )

    assert a == b
