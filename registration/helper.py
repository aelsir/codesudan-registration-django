def valid_phone_number(phone_number):
    if len(phone_number) < 12:
        return False
    return True

def valid_pin(pin):
    if len(pin) != 1 or not pin.isnumeric():
        return False
    return True
    