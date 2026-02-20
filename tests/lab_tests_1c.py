import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6  # Test case from LeetCode example
    assert max_subarray_sum([1]) == 1                       # Test case with single element
    assert max_subarray_sum([-1]) == -1                     # Test case with single negative element
    assert max_subarray_sum([-2,-3,-1]) == -1              # Test case with all negative numbers
    assert max_subarray_sum([5,4,-1,7,8]) == 23            # Test case with positive numbers and one negative number
    assert max_subarray_sum([0,0,0]) == 0                   # Test case with all zeros

def test_max_subarray_sum_empty():
    with pytest.raises(IndexError):
        max_subarray_sum([])  # Test case with empty list should raise an error

def test_max_subarray_sum_all_negative():
    assert max_subarray_sum([-3, -2, -1]) == -1  # Test case with all negative numbers should return the least negative number

def test_max_subarray_sum_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10  # Test case with all positive numbers should return the sum of the entire array

def test_max_subarray_sum_mixed():
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7  # Test case with mixed positive and negative numbers

if __name__ == "__main__":
    pytest.main()