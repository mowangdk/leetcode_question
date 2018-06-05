#!/usr/bin/env python
# -*- coding: utf-8 -*-


def merge(p_list, p_start, p_mid, p_end):

    pass


def merge_sort(p_list, p_start, p_end):

    if p_start < p_end:
        mid = (p_start + p_end) >> 1
        merge_sort(p_list, p_start, mid)
        merge_sort(p_list, mid + 1, p_end)
        merge(p_list, p_start, mid, p_end)


if __name__ == '__main__':
    pass
