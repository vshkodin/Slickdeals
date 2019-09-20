import pytest
from tests.test_Slickdeals.core import method_test_case_one

class TestClass:

    @pytest.fixture(autouse=True)
    def setup(self, driver_init):
        self.driver = driver_init

    def test_case_one(self):
        method_test_case_one(self)






