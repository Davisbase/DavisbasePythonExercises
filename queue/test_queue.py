from nose.tools import *

class TestMyQueue:

    def test_empty_on_instantiation(self):
        myQueue = MyQueue()
        assert_true(myQueue.empty())

class MyQueue:

    def __init__(self):
        self._empty = True

    def empty(self):
        return self._empty