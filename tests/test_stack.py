# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from algos.stack import StackException, Stack


def test_raises_when_capacity_is_0():
    with pytest.raises(StackException) as ex_info:
        Stack(0)
    assert ex_info.value.message == \
        'Capacity must be an int > 0 or Stack.UNLIMITED'


def test_raises_when_capacity_is_under_minus_1():
    with pytest.raises(StackException) as ex_info:
        Stack(-2)
    assert ex_info.value.message == \
        'Capacity must be an int > 0 or Stack.UNLIMITED'


def test_push_adds_item():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1


def test_push_pop_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_raises_when_popping_empty():
    with pytest.raises(StackException) as ex_info:
        Stack().pop()
    assert ex_info.value.message == 'already empty'


def test_raises_when_pushing_full():
    with pytest.raises(StackException) as ex_info:
        stack = Stack(1)
        stack.push(1)
        stack.push(2)
    assert ex_info.value.message == 'already full'


def test_starts_empty():
    assert Stack().empty()


def test_empty_after_pop():
    stack = Stack()
    stack.push(1)
    stack.pop()
    assert stack.empty()


def test_not_empty_after_push():
    stack = Stack()
    stack.push(1)
    assert not stack.empty()


def test_full_after_push():
    stack = Stack(1)
    stack.push(1)
    assert stack.full()


def test_doesnt_start_full():
    assert not Stack().full()


def test_full_resets_after_pop():
    stack = Stack(1)
    stack.push(1)
    assert stack.full()
    stack.pop()
    assert not stack.full()


def test_unlimited_capacity_by_default():
    stack = Stack()
    for i in xrange(1000):
        stack.push(i)


def test_capacity_for_2():
    stack = Stack(2)
    stack.push(1)
    stack.push(2)
    assert stack.full()
