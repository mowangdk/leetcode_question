#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
多继承方法调用解决方案1， without super


这里D继承了方法m的两个冲突定义， 并且发出错误信息。然后D可以通过覆盖m来解决冲突，但是D的定义是什么？， 它可以
调用B的m， 然后调用C的m， 但是由于两个定义都调用了从A继承的m的定义， 因此A的m最终被调用两次，老python简单的
通过只取第一个来解决。

这种困境的传统结局方案如下， 将m的每个派生定义分为两部分， 部分实现_m, 它只保存一个类唯一的数据。以及一个完整的实现m
"""


class A(object):
    def m(self):
        print u"save A's data"


class B(A):
    def _m(self):
        print u"save B's data"

    def m(self):
        self._m()
        A.m(self)


class C(A):
    def _m(self):
        print u"save C's data"

    def m(self):
        self._m()
        A.m(self)


class D(B, C):
    def _m(self):
        print u"save D's data"

    def m(self):
        self._m()
        B._m(self)
        C._m(self)
        A.m(self)



"""
但是这种模式存在一些问题， 首先是额外方法调用激增， 然后，A的存在不再被视作B和C的实现细节，并且D类需要知道A类具体做什么。如果在
程序的未来版本中，我们想要从B和C中删除对A的依赖， 那么这样同样也会影响像D这样的派生类，(B._m， C._m 失效）
并且如果想为B和C添加一个基类， 它们所有的派生类也必须要更新

下面使用super解决这个问题

super 的第一个参数始终是它所在的类， 第二个参数总是self
"""


class A1(object):
    def m(self):
        print "Save A's data"


class B1(A):
    def m(self):
        print "save B's data"
        super(B1, self).m()


class C1(A):
    def m(self):
        print "save C's data"
        super(C1, self).m()


class D1(B, C):
    def m(self):
        print "save D's data"
        super(D1, self).m()


"""
D.__mro__ == (D, B, C, A, object)
super(D, self).m() 首先会调用 B.m(self),  因为B是mro数组中的下一个类，
super(B, self).m() 被调用，其中self是D的实例, 之后C是B的下一个
调用 super(C, self).m() 仍然使用D的mro，最后， A.m 被调用，并且在这个方法里面没有super()
"""


class Super(object):

    def __init__(self, type, obj=None):
        self.__type__ = type
        self.__obj__ = obj

    def __get__(self, obj, type=None):
        if self.__obj__ is None and obj is not None:
            return Super(self.__type__, obj)
        else:
            return self

    def __getattr__(self, attr):
        if isinstance(self.__obj__, self.__type__):
            starttype = self.__obj__.__class__
        else:
            starttype = self.__obj__
        mro = iter(starttype.__mro__)

        for cls in mro:
            if cls is self.__type__:
                break
        # mro 是一个 迭代器， 会从中断处运行
        for cls in mro:
            if attr in cls.__dict__:
                x = cls.__dict__[attr]
                if hasattr(x, "__get__"):
                    x = x.__get__(self.__obj__)
                return x
        raise AttributeError, attr


class ATest(object):
    def m(self):
        return "A"


class BTest(ATest):
    def m(self):
        return "B" + Super(BTest, self).m()


class CTest(ATest):
    def m(self):
        return "C" + Super(CTest, self).m()


class DTest(CTest, BTest):
    def m(self):
        return "D" + Super(DTest, self).m()


if __name__ == '__main__':
    print DTest().m()