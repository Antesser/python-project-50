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
    b = generate_diff('./tests/fixtures/first.yaml',
                      './tests/fixtures/second.yaml',
                      'string')

    assert len(a) == len(b)
