from gendiff import engine


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
    b = engine.generate_diff('./text/fixtures/first_plain.json',
                             './text/fixtures/second_plain.json')

    assert len(a) == len(b)
