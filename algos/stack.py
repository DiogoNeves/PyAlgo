# !/usr/bin/env python
# -*- coding: utf-8 -*-
from algos import CollectionException, Collection, UNLIMITED


class StackException(CollectionException):
    pass


class Stack(Collection):
    def __init__(self, capacity=-1):
        if capacity == 0 or capacity < UNLIMITED:
            raise StackException(
                'Capacity must be an int > 0 or Stack.UNLIMITED')
        self._capacity = capacity
        self._stack = []

    def push(self, item):
        if self.full():
            raise StackException('already full')
        else:
            self._stack.append(item)

    def pop(self):
        if self.empty():
            raise StackException('already empty')
        else:
            return self._stack.pop()

    def empty(self):
        return len(self._stack) == 0

    def full(self):
        return len(self._stack) == self._capacity
