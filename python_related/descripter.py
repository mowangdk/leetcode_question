#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/3/15 上午11:41


class Question(object):

    def __init__(self):
        self.stem = ""
        self.score = 0
        self.description = "Qestion has {} stem , {} score".format(self.stem, self.score)

    def __get__(self, instance, owner):
        return instance.description

    def __set__(self, instance, value):
        if isinstance(value, tuple):
            instance.stem = value[0]
            if 10 < value[1] < 100:
                instance.score = value[1]
                instance.description = "Qestion has {} stem , {} score".format(instance.stem, instance.score)
            else:
                raise ValueError('score must between 10 and 100')


class Solution(object):
    # question = Question()
    def __new__(cls, *args, **kwargs):
        cls.question = Question()
        super(cls, Solution).__new__(*args, **kwargs)

    def __init__(self, question_data):
        self.question = question_data

    def __call__(self, *args, **kwargs):
        return args[0] + 1


class Grade(object):
    def __init__(self):
        self._score = 0

    def __get__(self, instance, owner):
        return self._score

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError('grade must be between 0 and 100')


class Exam(object):
    math = Grade()

    def __init__(self, math):
        self.math = math


if __name__ == '__main__':
    solution = Solution(("test get & set", 130))
    # solution.__call__ = lambda x: x + 1
    print solution.question
    # niche = Exam(120)
    # print niche.math

