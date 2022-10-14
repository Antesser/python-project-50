from gendiff.engine import generate_diff


def test_nested():
    a = open('./tests/fixtures/answer_nested.txt')
    b = generate_diff(
        './tests/fixtures/first_nested.json',
        './tests/fixtures/second_nested.json',
        'string'
    )

    assert a == b
