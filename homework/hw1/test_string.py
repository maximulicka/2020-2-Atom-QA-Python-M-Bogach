import pytest

parametrs = ['s1, template, replacement, result',
[('I started learning automated testing', 'I', 'Max', 'Max started learning automated testing'),
('I started learning automated testing', 'I', 'Nick', 'Nick started learning automated testing')]]


class TestString:
    
    def test_concat(self):
        s1 = 'test' 
        s2 = 'string'
        assert s1 + s2 == 'teststring'

    def test_length(self):
        s1 = 'string'
        assert len(s1) == 6

    def test_split(self):
        s1 = 'automated testing courses'
        s1_new = s1.split()
        assert s1_new == ['automated', 'testing', 'courses']

    def test_multiplication(self):
        s1 = 'test'
        assert 3 * s1 == 'testtesttest'

    @pytest.mark.parametrize(*parametrs)
    def test_replace(self, s1, template, replacement, result):
        s2 = s1.replace(template, replacement)
        assert s2 == result