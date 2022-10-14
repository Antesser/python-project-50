from gendiff.engine import generate_diff


def tests_yaml():
    a = open('./tests/fixtures/answer_plain.txt')
    b = generate_diff('./tests/fixtures/first_nested.json',
                      './tests/fixtures/second_nested.json',
                      'plain')

    assert a == b
