#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/3 下午8:23

import csv


def reading_csv(file1, file2):
    csv1_file = open(file1, 'r')
    csv2_file = open(file2, 'r')
    csv1_reader = csv.reader(csv1_file)
    csv2_reader = csv.reader(csv2_file)
    csv1_double_list = list()
    csv2_double_list = list()
    for index, line in enumerate(csv1_reader):
        csv1_double_list.append(line)
    for index, line in enumerate(csv2_reader):
        csv2_double_list.append(line)

    print csv1_double_list
    print csv2_double_list


if __name__ == '__main__':
    file1 = 'class1.csv'
    file2 = 'class2.csv'
    reading_csv(file1, file2)