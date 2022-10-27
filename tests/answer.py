YAML = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

NESTED_JSON = '''[{"key": "common", "status": "nested", "value": [{"key": "follow", "status": "added", "value": false}, {"key": "setting1", "status": "unchanged", "value": "Value 1"}, {"key": "setting2", "status": "deleted", "value": 200}, {"key": "setting3", "status": "changed", "value": {"old_value": true, "new_value": null}}, {"key": "setting4", "status": "added", "value": "blah blah"}, {"key": "setting5", "status": "added", "value": {"key5": "value5"}}, {"key": "setting6", "status": "nested", "value": [{"key": "doge", "status": "nested", "value": [{"key": "wow", "status": "changed", "value": {"old_value": "", "new_value": "so much"}}]}, {"key": "key", "status": "unchanged", "value": "value"}, {"key": "ops", "status": "added", "value": "vops"}]}]}, {"key": "group1", "status": "nested", "value": [{"key": "baz", "status": "changed", "value": {"old_value": "bas", "new_value": "bars"}}, {"key": "foo", "status": "unchanged", "value": "bar"}, {"key": "nest", "status": "changed", "value": {"old_value": {"key": "value"}, "new_value": "str"}}]}, {"key": "group2", "status": "deleted", "value": {"abc": 12345, "deep": {"id": 45}}}, {"key": "group3", "status": "added", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}}]'''  # noqa: E501

PLAIN = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

NESTED = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''  # noqa: W291
