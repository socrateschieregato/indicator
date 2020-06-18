

def is_stable(value):
    if value == 1:
        return False
    else:
        return True


def parse_to_float(value):
    return float(value.replace('\r\n', ''))
