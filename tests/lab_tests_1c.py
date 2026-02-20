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
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2  # Test case with all negative numbers where the least negative is the answer

if __name__ == "__main__":
    pytest.main()