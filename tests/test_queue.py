# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from algos.queue import QueueException, Queue


def test_raises_on_capacity_0():
    with pytest.raises(QueueException) as ex_info:
        Queue(0)
    assert ex_info.value.message == \
        'Capacity must be an int > 0 or Queue.UNLIMITED'


def test_raises_on_capacity_under_minus_1():
    with pytest.raises(QueueException) as ex_info:
        Queue(-2)
    assert ex_info.value.message == \
        'Capacity must be an int > 0 or Queue.UNLIMITED'


def test_starts_empty():
    assert Queue().empty()


def test_empty_after_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.dequeue()
    assert queue.empty()


def test_not_empty_after_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert not queue.empty()


def test_doesnt_start_full():
    assert not Queue().full()


def test_full_after_enqueue():
    queue = Queue(1)
    queue.enqueue(1)
    assert queue.full()


def test_not_full_after_dequeue():
    queue = Queue(1)
    queue.enqueue(1)
    queue.dequeue()
    assert not queue.full()


def test_enqueue_multiple_in_right_order():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


def test_raises_enqueuing_when_full():
    queue = Queue(1)
    with pytest.raises(QueueException) as ex_info:
        queue.enqueue(1)
        queue.enqueue(2)
    assert ex_info.value.message == 'already full'


def test_raises_dequeuing_empty():
    queue = Queue()
    with pytest.raises(QueueException) as ex_info:
        queue.dequeue()
    assert ex_info.value.message == 'already empty'


def test_peek_is_same_value_as_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == queue.dequeue()


def test_peek_when_empty_raises():
    with pytest.raises(QueueException) as ex_info:
        Queue().peek()
    assert ex_info.value.message == 'already empty'


def test_capacity_more_than_1():
    queue = Queue(2)
    with pytest.raises(QueueException) as ex_info:
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
    assert ex_info.value.message == 'already full'


def test_unlimited_by_default():
    queue = Queue()
    for i in xrange(1000):
        queue.enqueue(i)
    assert not queue.full()
