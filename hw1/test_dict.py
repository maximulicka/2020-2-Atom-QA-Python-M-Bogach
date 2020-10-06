import pytest

parametrs = [
    'dictionary, dict_update, result', [({a: a ** 2 for a in range(7)}, 
    {7: 49}, 
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}),
    ({a: a ** 2 for a in range(7)},
    {7: [49, 64]},
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: [49, 64]})]
]

class TestDict:

    def test_dictvalues(self):
        dictionary = {a: a ** 2 for a in range(7)}
        val = dictionary.values()
        assert list(val) == [0, 1, 4, 9, 16, 25, 36]

    def test_dictpop(self):
        dictionary = {a: a ** 2 for a in range(7)}
        dictionary.pop(3)
        assert dictionary == {0: 0, 1: 1, 2: 4, 4: 16, 5: 25, 6: 36}

    def test_dictclear(self):
        dictionary = {a: a ** 2 for a in range(7)}
        dictionary.clear()
        assert dictionary == {}
    
    def test_dictget(self):
        dictionary = {a: a ** 2 for a in range(7)}
        val = dictionary.get(3)
        assert val == 9

    @pytest.mark.parametrize(*parametrs)
    def test_dicupdate(self, dictionary, dict_update, result):
        dictionary.update(dict_update)
        assert dictionary == result




