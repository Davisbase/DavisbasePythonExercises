import unittest
from nose.tools import assert_equals, assert_true, assert_false

class TestMyQueue:

    def setUp(self):
        self.myQueue = MyQueue()

    def test_empty_on_instantiation(self):
        assert_true(self.myQueue.empty())

    def test_enqueue_sets_empty_false(self):
        self.myQueue.enqueue('some time')
        assert_false(self.myQueue.empty())

    def test_enqueue_then_dequeue_returns_to_empty(self):
        self.myQueue.enqueue('some item')
        self.myQueue.dequeue()
        assert_true(self.myQueue.empty())

    def test_dequeue_returns_correct_obj(self):
        expected_item = 'an item'
        self.myQueue.enqueue(expected_item)
        returned_item = self.myQueue.dequeue()
        assert_equals(expected_item, returned_item)

    def test_dequeue_order(self):
        items = ['a','b','c']
        for item in items:
            self.myQueue.enqueue(item)

        assert_equals(items[0],self.myQueue.dequeue())
        assert_equals(items[1],self.myQueue.dequeue())
        assert_equals(items[2],self.myQueue.dequeue())

    def test_dequeue_empty_queue(self):
        assert_raises(ValueError, self.myQueue.dequeue())

    def test_peek_makes_no_changes(self):
        expected_item = 'an item'
        self.myQueue.enqueue(expected_item)
        self.myQueue.peek()
        assert_false(self.myQueue.empty())

    def test_peek_has_right_value(self):
        expected_item = 'an item'
        self.myQueue.enqueue(expected_item)
        peeked_item = self.myQueue.peek()
        assert_equals(expected_item, peeked_item)

class MyQueue:

    def __init__(self):
        self._empty = True

    def empty(self):
        return self._empty

    def enqueue(self, item):
        self._empty = False

    def dequeue(self):
        return 'foo'
