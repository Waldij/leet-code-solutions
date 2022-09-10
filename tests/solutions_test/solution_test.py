import pytest
from solutions.temperatures.temperatures import solution, alternative_solution

TEST_CASES = [
    ([13, 12, 15, 11, 9, 12, 16], [2, 1, 4, 2, 1, 1, None]),
    ([13, 12, 15], [2, 1, None]),
    ([1, 2, 3], [1, 1, None]),
    ([3, 2, 1], [None, None, None]),
]


class TestSolution:
    """Test solution function. """
    @pytest.mark.parametrize('input_data, output_data', TEST_CASES)
    def test_solution(self, input_data, output_data, mr_printer):
        assert solution(input_data) == output_data


class TestAlternativeSolution:
    """Test alt solution function. """

    @pytest.mark.parametrize('input_data, output_data', TEST_CASES)
    def test_alt_solution(self, input_data, output_data, mr_printer):
        assert alternative_solution(input_data) == output_data
