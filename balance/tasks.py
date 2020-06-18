import serial
from balance.helpers import is_stable, parse_to_float
from utils.exceptions import SerialNotFound


def read_weight_by_serial_port():
    a = False
    try:
        with serial.Serial('COM3', baudrate=9600) as ser:
            while not a:
                count = 0
                for i in range(1, 10):
                    current_value = (ser.read_until()).decode('utf-8').split(',')

                    if len(current_value) < 4:
                        continue

                    stable = parse_to_float(current_value[0])
                    gross_weight = parse_to_float(current_value[1])
                    tare = parse_to_float(current_value[2])
                    net_weight = parse_to_float(current_value[3])

                    if is_stable(stable):
                        if count == 10 and gross_weight > 0:
                            print(f'{stable} - weight ok -> {gross_weight} - {tare} - {net_weight}')
                            count = 0

                        else:
                            count += 1
                            print(f'{count} - processing...')
                    else:
                        print(f'{stable} - not stable, wait please')
    except Exception as e:
        print(f'Error - trying to conect, {e}')
        raise SerialNotFound
