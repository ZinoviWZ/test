import json
import pytest
import yaml
import allure

@pytest.fixture(scope="class")
def func():
    print("fixture前置")
    yield
    print("fixture后置")

@allure.step("这是测试第X步")
def add(a, b):
    return a + b

@allure.step("这是测试第X步")
def jian(a, b):
    return a - b

def getdata():
    with open("./a.yaml", encoding="utf-8") as f:
        param = yaml.safe_load(f)
    return param

@allure.epic("这是XXX系统")
@allure.feature("这是XXX功能模块")
class Test1:
    def setup_method(self):
        print("类中setup_class")

    def teardown_method(self):
        print("类中teardown_class")

    @allure.story("测试加法场景")
    @pytest.mark.parametrize("a,b,c", getdata())
    @allure.title("测试标题：{a} + {b} = {c}")
    def test_01(self, a, b, c):
        s = add(a, b)
        assert c == s

    @allure.story("测试减法场景")
    @pytest.mark.parametrize("a,b,c", getdata())
    @allure.title("测试标题：{a} - {b} = {c}")
    def test_02(self, a, b, c):
        s = add(a, b)
        assert c == s

if __name__ == '__main__':

    pytest.main()