from unittest import mock

from serial import Serial
import pytest

from balance.helpers import is_stable
from balance.tasks import read_weight_by_serial_port
from utils.exceptions import ReadSerialError


def test_read_weight_by_serial_port():
    with pytest.raises(Exception):
        read_weight_by_serial_port()


@mock.patch(
    'serial.Serial',
    return_value=Serial(
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=1,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False
    )
)
@mock.patch(
    'serial.SerialBase.read_until',
    return_value="0, 000.000, 000.000, 000.000\r\n".encode('utf-8')
)
def test_read_weight_by_serial_port_should_get_weight(mock_read_until, mock_serial):
    mock_serial.return_value.is_open = True

    assert read_weight_by_serial_port() == (0, 000.000, 000.000, 000.000)


@mock.patch(
    'serial.Serial',
    return_value=Serial(
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=1,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False
    )
)
@mock.patch(
    'serial.SerialBase.read_until',
    return_value="1, 000.000, 000.000, 000.000\r\n".encode('utf-8'))
def test_read_weight_by_serial_port_should_not_stable(mock_read_until, mock_serial):
    mock_serial.return_value.is_open = True

    assert not read_weight_by_serial_port()


@mock.patch(
    'serial.Serial',
    return_value=Serial(
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=1,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False
    )
)
@mock.patch(
    'serial.SerialBase.read_until',
    return_value="0, 001.000, 000.500, 000.500\r\n".encode('utf-8'))
def test_read_weight_by_serial_port_with_tare(mock_read_until, mock_serial):
    mock_serial.return_value.is_open = True

    assert read_weight_by_serial_port() == (0, 001.000, 000.500, 000.500)


@mock.patch(
    'serial.Serial',
    return_value=Serial(
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=1,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False
    )
)
def test_read_weight_by_serial_port_with_no_data(mock_serial):
    mock_serial.return_value.is_open = True
    with pytest.raises(ReadSerialError):
        read_weight_by_serial_port()


def test_is_stable_true():
    assert is_stable(0)


def test_is_stable_false():
    assert not is_stable(1)
