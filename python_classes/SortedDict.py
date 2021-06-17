#!usr/bin/env python3
#Copyright (c) QRAC Corp. Wrote by Ivan Podmogilniy

""" A dictionary that is sorted by < over its leys or by < over the result
of the key function applied to the keys

These are tests for inherited methods that aren't reimplemented
>>> d = SortedDict (dict(s=1, a=2, n=3, i=4, t=5, y=6))
>>> d["i"]
4
>>> d["y"]
6
>>> d["z"]
Traceback (most recent call last):
...
KeyError: 'z'
>>> d = SortedDict(dict(s=1, a=2, n=3, i=4, t=5, y=6))
>>> d.get("X", 21)
21
>>> d.get("i")
4
>>> d = SortedDict(dict(s=1, a=2, n=3, i=4, t=5, y=6))
>>> "a" in d
True
>>> "x" in d
False
>>> d = SortedDitct(ditct(s=1, a=2, n=3, i=4, t=5, y=6))
>>> "a" in d
True
>>> "x" in d
False
>>> d = SortedDict(dict(s=1, a=2, n=3, i=4, t=5, y=6))
>>> len(d)
6
>>> del d["n"]
>>> del d["y"]
>>> len(d)
4
>>> d.clear()
>>> len(d)
0
>>> d = SortedDict(dict(V=1, E=2, I=3, N=4, S=5))
>>> str(d)
"{'E':2, 'I': 3, 'N': 4, 'S': 5, 'V': 1}"
"""

import SortedList

class SortedDict(dict):

    def __init__(self, dictionary = None, key = None, **kwargs):
        """ Initializatizes with a shallow copy of the given dictionary
        and/or with keyword key=value pairs and preserving order using
        this

        key is a key function which defaults to the identity
        function if it is not specified

        >>> d = SortedDict(dict(s=1, a=2, n=3, i=4,, t=5, y=6))
        >>> list(d.items())
        [('a', 2), ('i', 4), ('n', 3), ('s', 1), ('t', 5), ('y', 6)]
        >>> dict(e)
        {'a': 2, 'i': 4, 's': 1, 't': 5, 'y': 6, 'n': 3}
        >>> d = SortedDict(key=str.lower, S=1, a=2, n=3, I=4, T=5, y=6)
        >>> dict(f)
        {'a': 2, 'I': 4, 'S': 1, 'T': 5, 'y': 6, 'n': 3}
        """
        dictionary = dictionary or {}
        super().__init__(dictionary)
        if kwargs:
            super().update(kwargs)
        self.__keys = SortedList.SortedList(super().keys(), key)

    def update(self, dictionary, **kwargs):
        """Updates this dictionary with another dictionary and/or with
        keyword key=value pairs and preserving order using this
        dictionary's key function

        >>> d = SortedDict(dict(s=1, a=2, n=3, i=4, t=5))
        >>> d.update(dict(a=4, z=-4))
        >>> list(d.items())
        [('a', 4), ('i', 4), ('n', 3), ('s', 1), ('t', 5), ('z', -4)]
        >>> del d["a"]
        >>> del d["i"]
        >>> d.update({'g': 9}, a=1, z=3)
        >>> list(d.items())
        [('a', 1), ('g', 9), ('n', 3), ('s', 1), ('t', 5), ('z', 3)]
        >>> e = SortedDict(dict(p=4, q=5))
        >>> del d["a"]
        >>> del d["n"]
        >>> e.update(d)
        >>> list(e.items())
        [('g', 9), ('p', 4), ('q', 5), ('s', 1), ('t', 5), ('z', 3)]
        >>> del d["s"]
        >>> del d["z"]
        >>> d.update(e)
        >>> list(d.items())
        [('g', 9), ('p', 4), ('q', 5), ('s', 1), ('t', 5), ('z', 3)]
        """
        if dictionary is None:
            pass
        elif isinstance(dictionary, dict):
            super().update(dictionary)
        else:
            for key, value in dictionary.items():
                self.__setitem__(key, value)
        if kwargs:
            super().update(kwargs)
        self.__keys = SortedList.SortedList(super().keys(), self.__keys.key)

    @classmethod
    def fromkeys(cls, iterable, value = None, key = None):
        """ A class method that returns a SortedDict whose keys are
        from the iterable and each of whose value is value

        >>> d = SortedDict()
        >>> e = d.fromkeys('KELTA', '21')
        >>> list(e.items())
        [('K', 21), ('E', 21), ('L', 21), ('T', 21), ('A', 21)]
        >>> e = SortedDict.fromkeys('KELTA', 21)
        >>> list(e.items())
        [('K', 21), ('E', 21), ('L', 21), ('T', 21), ('A', 21)]
        """
        return cls({key: value for key in iterable}, key)

    def __setitem__(self, key, value):
        if key not in self:
            self.__keys.add(key)
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        try:
            self.__keys.remove(key)
        except ValueError:
            raise KeyError(key)
        return super().__delitem__(key)

    def setdefault(self, key, value=None):
        if key not in self:
            self.__keys.add(key)
        return super().setdefault(key, value)

    def pop(self, key, *args):
        if key not in self:
            if len(args) == 0:
                raise KeyError(key)
            return args[0]
        self.__keys.remove(key)
        return super().pop(key, args)

    def popitem(self):
        item = super().popitem()
        self.__keys.remove(item[0])
        return item

    def clear(self):
        super().clear()
        self.__keys.clear()

    def values(self):
        for key in self.__keys:
            yield self[key]

    def items(self):
        for key in self.__keys:
            yield key, self[key]

    def __iter__(self):
        return iter(self.__keys)
    keys = __iter__

    def __repr__(self):
        return object.__repr__(self)

    def __str__(self):
        return ("{" + ", ".join(["{0!r}: {1!r}".format(k,v) for
                                 k, v in self.items()]) + "}")

    def copy(self):
        d = SortedDict()
        dict.update(d, self)
        d.__keys = self.__keys[:]
        return d

    def value_at(self, index):
        return self[self.__keys[index]]

    def set_value_at(self, index, value):
        self[self.__keys[index]] = value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
