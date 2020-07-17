import pytest
import tempfile

ENCODING = 'utf-8'

@pytest.fixture
def load_data_from_disk():
    filepath = tempfile.NamedTemporaryFile().name
    with open(filepath, 'wb') as stream:
        stream.write(b'something')

    with open(filepath, 'rb') as stream:
        return stream.read().decode(ENCODING)

