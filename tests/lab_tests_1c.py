import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6  # Test case from LeetCode problem
    assert max_subarray_sum([1]) == 1                       # Test for single element
    assert max_subarray_sum([-1]) == -1                     # Test for single negative element
    assert max_subarray_sum([-2,-3,-1]) == -1              # Test for all negative elements
    assert max_subarray_sum([5,4,-1,7,8]) == 23            # Test for all positive elements
    assert max_subarray_sum([-2,1]) == 1                   # Test for two elements with one negative
    assert max_subarray_sum([-2,-3,4]) == 4                # Test for two negatives followed by a positive
    assert max_subarray_sum([0, -3, 1, 2]) == 3       # Test for zero followed by negatives and positives

def test_empty_array():
    with pytest.raises(IndexError):
        max_subarray_sum([])  # Test for empty array, should raise an error

def test_all_negative():
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2  # Test for all negative numbers, should return the least negative

def test_all_positive():
    assert max_subarray_sum([2, 3, 1, 5]) == 11  # Test for all positive numbers, should return the sum of the entire array

def test_mixed_numbers():
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7  # Test for mixed numbers, should return the maximum sum of a contiguous subarray

if __name__ == "__main__":
    pytest.main()