from gendiff.engine import generate_diff


answer = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def tests_json():
    a = answer
    b = generate_diff('./tests/fixtures/first.json',
                             './tests/fixtures/second.json')

    assert len(a) == len(b)
