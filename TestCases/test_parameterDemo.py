import pytest


@pytest.mark.parametrize("name,role", [('Ram', 'QA'), ['Shweta', 'Dev'], ['Ravi', 'Manager']])
def test_validation(name, role):
    assert name is not None
    assert role is not None


@pytest.fixture(scope='module', params=['www.google.com'])
def val(request):
    return request.param


def test_val(val):
    assert val == 'www.google.com'
