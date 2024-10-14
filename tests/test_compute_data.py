import numpy.testing as npt
import pytest
from pathlib import Path
import math
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inflammation.compute_data import analyse_data, CSVDataSource, compute_standard_deviation_by_day


# from python-intermediate-inflammation.inflammation import CSVDataSource


# from inflammation.compute_data import analyse_data





@pytest.mark.parametrize('data,expected_output', [
    ([[[0, 1, 0], [0, 2, 0]]], [0, 0, 0]),
    ([[[0, 2, 0]], [[0, 1, 0]]], [0, math.sqrt(0.25), 0]),
    ([[[0, 1, 0], [0, 2, 0]], [[0, 1, 0], [0, 2, 0]]], [0, 0, 0])
],
ids=['Two patients in same file', 'Two patients in different files', 'Two identical patients in two different files'])
def test_compute_standard_deviation_by_day(data, expected_output):
    result = compute_standard_deviation_by_day(data)
    npt.assert_array_almost_equal(result, expected_output)