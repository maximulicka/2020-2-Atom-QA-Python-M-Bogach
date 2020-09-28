import pytest

parametrs = [
    'input_, symbol_append, result', [([7, 8, 9], [5], [7, 8, 9, [5]]), 
([7, 8, 9], 101, [7, 8, 9, 101])]
]

class TestList:
    
    def test_reverse(self):
        input_ = [7, 8, 9]
        input_.reverse()
        assert input_ == [9, 8, 7]

    def test_sort(self):
        input_ = [9, 7, 8]
        input_.sort()
        assert input_ == [7, 8, 9]

    def test_insert(self):
        input_ = [7, 8, 9]
        input_.insert(2,25)
        assert input_ == [7, 8, 25, 9]

    def test_multiplication(self):
        input_ = [7, 8, 9]
        assert 3 * input_ == [7, 8, 9, 7, 8, 9, 7, 8, 9]

    @pytest.mark.parametrize(*parametrs)
    def test_append(self, input_, symbol_append, result):
        input_.append(symbol_append)
        assert input_ == result