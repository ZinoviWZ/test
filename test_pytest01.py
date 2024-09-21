import json
import pytest
import yaml

@pytest.fixture(scope="class")
def func():
    print("fixture前置")
    yield
    print("fixture后置")

def add(a, b):
    return a + b

def getdata():
    with open("./a.yaml", encoding="utf-8") as f:
        param = yaml.safe_load(f)
    return param

@pytest.mark.parametrize("a,b", getdata())
def test_01(a,b):
    s = add(a,b)
    assert 2 == s

@pytest.mark.parametrize("a,b", getdata())
def test_02(a,b):
    s = add(a,b)
    assert 29 == s


class Test1:
    def setup_method(self):
        print("类中setup_class")

    def teardown_method(self):
        print("类中teardown_class")

    @pytest.mark.parametrize("a,b", getdata())
    def test_03(self, func, a,b):
        s = add(a,b)
        assert 2 == s

    @pytest.mark.parametrize("a,b", getdata())
    def test_04(self, a, b):
        s = add(a, b)
        assert 7 == s

if __name__ == '__main__':

    pytest.main()