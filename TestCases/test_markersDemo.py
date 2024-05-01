import pytest


@pytest.mark.login
@pytest.mark.regression
def test_regression1():
    print('Test1')


@pytest.mark.sanity
def test_regression2():
    print('Test2')


@pytest.mark.xfail
def test_regression3():
    print('Test3')
    assert 4 == 5
