import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]          # Test case from LeetCode example
    assert two_sum([3, 2, 4], 6) == [1, 2]               # Test case with multiple pairs
    assert two_sum([3, 3], 6) == [0, 1]                  # Test case with duplicate numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4] # Test case with negative numbers
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]          # Test case with zeros

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 7) == []                   # Test case with no solution

def test_two_sum_single_element():
    assert two_sum([1], 1) == []                        # Test case with single element, no solution

def test_two_sum_large_numbers():
    assert two_sum([1000000000, 999999999], 1999999999) == [0, 1]  # Test case with large numbers

def test_two_sum_negative_target(): 
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]         # Test case with negative target

if __name__ == "__main__":
    pytest.main()