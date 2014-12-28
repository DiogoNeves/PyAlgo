# !/usr/bin/env python
# -*- coding: utf-8 -*-
from algos import CollectionException, Collection, UNLIMITED


class QueueException(CollectionException):
    pass


class Queue(Collection):
    def __init__(self, capacity=UNLIMITED):
        if capacity == 0 or capacity < UNLIMITED:
            raise QueueException(
                'Capacity must be an int > 0 or Queue.UNLIMITED')
        self._capacity = capacity
        self._queue = []

    def enqueue(self, item):
        if self.full():
            raise QueueException('already full')
        self._queue.insert(0, item)

    def dequeue(self):
        if self.empty():
            raise QueueException('already empty')
        return self._queue.pop()

    def peek(self):
        if self.empty():
            raise QueueException('already empty')
        return self._queue[-1]

    def empty(self):
        return len(self._queue) == 0

    def full(self):
        return len(self._queue) == self._capacity
