import allure
import pytest


@allure.suite("Other API")
class TestOther:

    @allure.title("Test expected to fail")
    def test_to_fail(self):
        with allure.step("Verification step"):
            assert 4 == 5

    @allure.title("Test expected to pass")
    def test_to_pass(self):
        with allure.step("Verification step"):
            a = 5
            assert a == 5
