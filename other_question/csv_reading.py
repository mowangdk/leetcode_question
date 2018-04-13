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
    csv1_header = csv1_double_list[0]
    csv2_header = csv2_double_list[0]
    csv1_id_index = csv1_header.index('id')
    csv2_id_index = csv2_header.index('id')
    conbine_head_list = list(set(csv2_header) | set(csv1_header))
    conbine_double_list = list()
    conbine_double_list.append(conbine_head_list)
    for row_number in range(1, max(len(csv1_double_list), len(csv2_double_list))):
        csv1_row_data = csv1_double_list[row_number]
        csv2_row_data = csv2_double_list[row_number]
        conbine_row_data = []
        ano_conbine_row_data = []
        for index in range(len(conbine_head_list)):
            csv1_index = -1
            csv2_index = -1
            if csv1_row_data[csv1_id_index] == csv2_row_data[csv2_id_index]:
                current_header = conbine_head_list[index]
                if current_header in csv1_header:
                    csv1_index = csv1_header.index(current_header)
                if current_header in csv2_header:
                    csv2_index = csv2_header.index(current_header)
                if csv1_index != -1 and csv2_index != -1:
                    if csv1_row_data[csv1_index] == csv2_row_data[csv2_index]:
                        conbine_row_data.append(csv1_row_data[csv1_index])
                    else:
                        raise Exception('data complex')
                elif csv1_index != -1:
                    conbine_row_data.append(csv1_row_data[csv1_index])
                elif csv2_index != -1:
                    conbine_row_data.append(csv2_row_data[csv2_index])
            else:
                current_header = conbine_head_list[index]
                if current_header in csv1_header:
                    csv1_index = csv1_header.index(current_header)
                    conbine_row_data.append(csv1_row_data[csv1_index])
                else:
                    conbine_row_data.append('')
                if current_header in csv2_header:
                    csv2_index = csv2_header.index(current_header)
                    ano_conbine_row_data.append(csv2_row_data[csv2_index])
                else:
                    ano_conbine_row_data.append('')
        conbine_double_list.append(conbine_row_data)
        if ano_conbine_row_data:
            conbine_double_list.append(ano_conbine_row_data)


if __name__ == '__main__':
    file1 = 'class1.csv'
    file2 = 'class2.csv'
    reading_csv(file1, file2)