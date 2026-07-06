"""
Fixtures - fixtures provide a way to create reusable setup code so that we can share that reusable
code across multiple test cases.
"""
import pytest


# @pytest.fixture
# def pre_setup():
#     print("I setup browser instance")
#
#
# def test_initial_check(pre_setup):
#     print("This is first test")
#
# def test_second_check(pre_setup):
#     print("This is second test")

# Fixture Scopes
# 1. Module - runs only once for the entire test file

@pytest.fixture(scope = "module")
def pre_setup():
    print("I setup browser module instance")
    return "pass"

@pytest.fixture(scope = "function")
def pre_setup2():
    print("I setup second browser function instance")
    yield
    print("I teardown browser function instance")

@pytest.mark.regression
def test_initial_check(pre_setup, pre_setup2):
    print("This is first test")

# @pytest.mark.skip - To skip a test
@pytest.mark.smoke
def test_second_check(pre_setup, pre_setup2):
    print("This is second test")
    assert  pre_setup == "pass"

# 2. Function - runs once for each test

# @pytest.fixture
# def pre_setup(scope = "function"):
#     print("I setup browser instance")
#
#
# def test_initial_check(pre_setup):
#     print("This is first test")
#
# def test_second_check(pre_setup):
#     print("This is second test")

# 3. Class - runs once for your entire class - We need to use if you write your tests in a class

# 4. Session - runs only once for the execution or session
#Eg - Launching browser for all the test cases
