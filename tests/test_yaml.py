from gendiff.engine import generate_diff


def tests_yaml():
    a = './tests/fixtures/answer_j.answer_j.y.json'
    b = generate_diff('./tests/fixtures/first.json',
                      './tests/fixtures/second.json',
                      'string')

    assert a == b
