"""Test core functionalities."""

from pytest_constants import ENCODING
from pytest_helpers import load_data_from_disk

# TODO: Replace with real tests.
def test_version():
    from exovetter import __version__
    assert __version__


def test_loading_data(load_data_from_disk):
    assert not isinstance(load_data_from_disk, None.__class__)

def test_encoding(load_data_from_disk):
    assert load_data_from_disk != load_data_from_disk.decode(ENCODING)

