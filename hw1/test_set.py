import pytest

parametrs = [
    'set1, set2, res', [(set('test'), set('python'), {'e', 'h', 'n', 'o', 'p', 's', 't', 'y'}),
    (set([5, 6]), set([7]), {5, 6, 7})]
]

class TestSet:

    def test_add(self):
        input_ = set('abc')
        input_.add('b')
        assert input_ == {'a', 'b', 'c'}

    def test_intersection(self):
        input_1 = set('abc')
        input_2 = set('d')
        res = input_1.intersection(input_2)
        assert res == set()

    def test_remove(self):
        input_ = set('abc')
        input_.remove('b')
        assert input_ == {'a', 'c'}

    def test_in(self):
        input_ = set('abc')
        res = 'b' in input_
        assert res == True

    @pytest.mark.parametrize(*parametrs)
    def test_union(self, set1, set2, res):
        set3 = set1.union(set2)
        assert set3 == res