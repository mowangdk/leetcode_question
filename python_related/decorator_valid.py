#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/17 下午9:01


class ValidateUtils(object):

    COMMON = 'COMMON'
    EDIT = 'EDIT'
    ONLINE = 'ONLINE'
    PRE = 'PRE'
    RELEASE = 'RELEASE'

    @classmethod
    def validate_for(cls, type_names):
        """
        装饰函数， 用于给ValidatePaper的方法设置对象类型
        :param type_names:
        :return:
        """
        def decorator(f):
            setattr(f, 'validate_types', type_names)
            return f
        return decorator

    @classmethod
    def is_type(cls, f, type_name):
        """
        是否某类型的校验
        :param f:
        :param type_name:
        :return:
        """
        return f and hasattr(f, 'validate_types') and type_name in f.validate_types


class ValidatePaper(object):

    def validate_for_release(self):
        msgs = list()
        for f in self.__class__.__dict__.values():
            if ValidateUtils.is_type(f, ValidateUtils.COMMON) or ValidateUtils.is_type(f, ValidateUtils.RELEASE):
                msg = f(self)
                if msg:
                    msgs.append(msg)
        return msgs

    @ValidateUtils.validate_for([ValidateUtils.COMMON, ValidateUtils.EDIT])
    def title(self):
        """
        对于标题的校验
        :return:
        """
        if not self.doc.title:
            return u'错误： 试卷标题不能为空'

    @ValidateUtils.validate_for([ValidateUtils.COMMON])
    def data(self):
        if not self.doc.date:
            return u"错误， 试卷日期不能为空"


