import serial
from balance.helpers import is_stable, parse_to_float
from utils.exceptions import SerialNotFound, ReadSerialError

TIMEOUT = 5


def read_weight_by_serial_port(port='COM4'):
    try:
        with serial.Serial(port, baudrate=9600, timeout=1) as ser:
            if not ser:
                raise SerialNotFound
            count = 0
            try:
                for i in range(1, 15):
                    current_value = (ser.read_until()).decode('utf-8').split(',')

                    if current_value == ['']:
                        raise ReadSerialError

                    if len(current_value) < 4:
                        continue

                    digit = parse_to_float(current_value[0])
                    gross_weight = parse_to_float(current_value[1])
                    tare = parse_to_float(current_value[2])
                    net_weight = parse_to_float(current_value[3])

                    if is_stable(digit):
                        if count >= 10 and gross_weight >= 0:
                            print(f'{int(digit)} - weight ok -> {gross_weight} - {tare} - {net_weight}')
                            return digit, gross_weight, tare, net_weight

                        else:
                            count += 1
                    else:
                        print(f'{int(digit)} - not stable, please wait')
            except Exception:
                raise ReadSerialError
    except ReadSerialError:
        raise ReadSerialError

    except Exception as e:
        print(f'Error - trying to connect, {e}')
        raise SerialNotFound
