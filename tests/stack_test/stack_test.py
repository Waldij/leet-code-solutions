import pytest
from typing import List, Any

from solutions.temperatures.helpers.stack import Stack
from tests.stack_test.data import StackBaseTestData, StackMethodsTestData


class TestStack:
    @pytest.mark.parametrize('data, as_list', [
        (StackBaseTestData.BASE,
         StackMethodsTestData.AsList.AS_LIST),
    ])
    def test_as_list(self, data: List[Any], as_list: List[Any]):
        stack = Stack()
        TestStack.set_stack_from_list(stack, data)

        assert stack.as_list() == data

    @pytest.mark.parametrize('data, after_pop', [
        (StackBaseTestData.BASE,
         StackMethodsTestData.Pop.AFTER_POP),
    ])
    def test_pop(self, data, after_pop):
        stack = Stack()
        TestStack.set_stack_from_list(stack, data)

        stack.pop()
        assert stack.as_list() == after_pop

    @pytest.mark.parametrize('data, to_append, after_append', [
        (StackBaseTestData.BASE,
         StackMethodsTestData.Append.TO_APPEND,
         StackMethodsTestData.Append.AFTER_APPEND),
    ])
    def test_append(self, data, to_append, after_append):
        stack = Stack()
        TestStack.set_stack_from_list(stack, data)

        stack.append(to_append)

        assert stack.as_list() == after_append

    @pytest.mark.parametrize('data, peeked, after_peek', [
        (StackBaseTestData.BASE,
         StackMethodsTestData.Peek.PEEKED,
         StackMethodsTestData.Peek.AFTER_PEEK)
    ])
    def test_peek(self, data, peeked, after_peek):
        stack = Stack()
        TestStack.set_stack_from_list(stack, data)

        peeked_data = stack.peek()

        assert peeked_data == peeked
        assert stack.as_list() == after_peek

    @pytest.mark.parametrize('data, length_before, to_append, length_after', [
        (StackBaseTestData.BASE,
         StackBaseTestData.BASE_LENGTH,
         StackMethodsTestData.Length.TO_APPEND,
         StackMethodsTestData.Length.LENGTH_AFTER_APPEND)
    ])
    def test_length(self, data, length_before, to_append, length_after):
        stack = Stack()
        TestStack.set_stack_from_list(stack, data)

        assert len(stack) == length_before

        stack.append(to_append)
        assert len(stack) == length_after

    @pytest.mark.parametrize('data, as_string', [
        (StackBaseTestData.BASE,
         StackMethodsTestData.String.AS_STRING)
    ])
    def test_to_string(self, data, as_string):
        stack = Stack()
        TestStack.set_stack_from_list(stack, data)

        assert str(stack) == as_string

    @staticmethod
    def set_stack_from_list(stack: Stack, data_list: List[Any]) -> None:
        for data in data_list:
            stack.append(data)
