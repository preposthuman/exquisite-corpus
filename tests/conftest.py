import os

import pytest
from shutil import copytree, rmtree


def pytest_addoption(parser):
    parser.addoption('--quick', action='store_true', help='Use existing input files in'
                                                          ' tests/data')


@pytest.fixture(scope='session', name='is_quick_run')
def quick_run(pytestconfig):
    return pytestconfig.option.quick


@pytest.fixture(scope='session')
def setup_test_directory(is_quick_run):
    if not is_quick_run:
        rmtree('tests/data', ignore_errors=True)
        copytree('tests/input_data/', 'tests/data/')


@pytest.fixture(scope='session')
def test_env_variables():
    env_variables = os.environ.copy()
    env_variables['XC_BUILD_TEST'] = '1'
    return env_variables
