import allure
import pytest
from page.page import Page


class Test_allure:
    def setup(self):
        self.page = Page()
        pass

    def teardown(self):
        pass

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_login1(self):
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login2(self):
        assert 1

    def test_login3(self):
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_login4(self):
        assert 1
        assert 1

    def test_login5(self):
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_login6(self):
        assert 0
