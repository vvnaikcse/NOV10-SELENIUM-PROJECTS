import pytest
class testclass:
    @pytest.fixture()
    def setup(self):
        print("application setup method")
    def testmethod1(self,setup):
        print("method1")
    def testmethod2(self,setup):
        print("method2")
    def testmethod3(self,setup):
        print("method3")