from dataclasses import dataclass
from solutions.temperatures.helpers.stack import Stack


@dataclass
class Pair:
    value: int
    index: int


def solution(temperatures: list[int]) -> list:
    answer = [None for _ in range(len(temperatures))]
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[i] < temperatures[j]:
                answer[i] = j - i
                break
    return answer


def alternative_solution(temperatures: list[int]) -> list:
    result = [None for _ in range(len(temperatures))]
    stack = Stack()

    return result
