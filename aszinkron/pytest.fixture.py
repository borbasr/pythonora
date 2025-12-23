import pytest

@pytest.fixture
def sample_data():
    return {'key': 'value'}

def test_fixture_usage(sample_data):
    assert sample_data['key'] == 'value'
