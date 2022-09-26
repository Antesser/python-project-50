from gendiff.engine import generate_diff


answer = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def tests_yaml():
    a = answer
    b = generate_diff('./tests/fixtures/first_nested.json',
                      './tests/fixtures/second_nested.json',
                      'plain')

    assert len(a) == len(b)
