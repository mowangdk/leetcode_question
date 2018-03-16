#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/7 上午11:35
import numbers
from array import array

import math


class Vector(object):
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = repr(self._components)
        components = components[components.find('['):]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    # def __bytes__(self):

    def __eq__(self, other):
        return tuple(self) == tuple(self)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    # @classmethod
    # def frombytes(cls, octets):
    #     typecode = chr(octets[0])
    #     memv = memoryview(octets[1:]).cast(typecode)
    #     return cls(memv)
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=cls))

    # 当实例没有那一个名字的属性时， Python只会呼叫该方法来作为后备机制。但是在我们指派v.x = 10之后，
    # v物件有一个x属性， 所以__getattr__再也不会被呼叫
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = "{.__name__!r} object has no attribute"
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = "read only attribute {attr_name!r}"
            elif key.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super(Vector, self).__setattr__(key, value)


class A(dict):
    c1 = 'v1'


# 因为复写了__setattr__方法， 所以初始化的时候并没有将c3 set进B的实例中， 导致c3的属性一直为空, 同样b.c1, b.c2, b.c3 也没有设置成功，
# 仅仅是调用了__setitem__, 设置到对象里面去了

class B(A):
    c2 = 'v2'

    def __init__(self):
        self.c3 = 'v3'

    def __setattr__(self, key, value):
        self[key] = value
        # super(B, self).__setattr__(key, value)

    def __getattr__(self, key):
        return self[key]

    # def __setitem__(self, key, value):
    #     pass

    def echo(self):
        print self.c1
        print self.c2
        print self.c3


def interview_question():
    b = B()
    b.echo()
    print b
    if hasattr(b, 'c1'):
        print 'yes'
    else:
        print 'no'
    b.c1 = "cv1"
    b.c2 = "cv2"
    b.c3 = "cv3"
    b.echo()
    print b


def vector_test():
    v = Vector(range(5))
    print v
    print v.x
    v.x = 10
    print v.x
    print v

if __name__ == '__main__':
    interview_question()
    # vector_test()
