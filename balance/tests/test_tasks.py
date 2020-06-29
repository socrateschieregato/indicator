from unittest import mock

import pytest

from balance.helpers import is_stable
from balance.tasks import read_weight_by_serial_port


def test_read_weight_by_serial_port():
    with pytest.raises(Exception):
        read_weight_by_serial_port()

def test_read_weight_by_serial_port():
    port = mock.Mock()
    port.readline = mock.Mock(
        return_value="0, 000.000, 000.000, 000.000\r\n".encode('utf-8')
    )

    assert read_weight_by_serial_port() == "my string"


def test_is_stable_true():
    assert is_stable(0)


def test_is_stable_false():
    assert not is_stable(1)
