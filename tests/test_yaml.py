from gendiff.engine import generate_diff


def tests_yaml():
    a = open('./tests/fixtures/answer_j.answer_j.y.txt')
    b = generate_diff('./tests/fixtures/first.json',
                      './tests/fixtures/second.json',
                      'string')

    assert a == b
