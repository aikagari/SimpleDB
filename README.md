# SimpleDB

Simple key-value db. Based on json.

## Usage

```python
In [1]: from simpledb import SimpleDB

In [2]: db = SimpleDB('test')

In [3]: db.set('item', 123)
Out[3]: True

In [4]: db.get('item')
Out[4]: 123

In [5]: db.get('item_2')

In [6]: db.has('item')
Out[6]: True

In [7]: db.pop('item')
Out[7]: 123

In [8]: db.has('item')
Out[8]: False

In [9]: db.set('a', 1)
Out[9]: True

In [10]: db.delete('a')
Out[10]: True

In [11]: db.has('a')
Out[11]: False
```

## Todo

- Support list as value
- Dump data on exit
- Add autodump on changes or use dump on schedule
- Add tests
- Add mode, if file is broken, force create new
- Add some methods for len keys, drop changes and load last saved version
