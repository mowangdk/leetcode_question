#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def Max_Heapify(heap, HeapSize, root):
    # 在堆中做结构使得父节点的值大于子节点

    left = 2 * root + 1
    right = left + 1
    larger = root

    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right

    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        Max_Heapify(heap, HeapSize, larger)


def Build_Max_Heap(heap):
    # 构造一个堆，将堆中所有的数据重新排序
    HeapSize = len(heap)
    for i in xrange((HeapSize - 2)//2, -1, -1):
        Max_Heapify(heap, HeapSize, i)


def HeapSort(heap):
    Build_Max_Heap(heap)
    # HeapSize 从高到底，逐渐递减
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[1] = heap[1], heap[0]
        Max_Heapify(heap, i, 0)
    return heap


if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print a
    HeapSort(a)
    print a
    b = [random.randint(1, 1000) for i in range(1000)]
    print b
    HeapSort(b)
    print b