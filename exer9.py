class HexFormatError(Exception):
    "Raised if the string does not fit with the format for hexadecimal."
    pass

class MemoryError(Exception):
    "Raised if the string is beyond 4-bytes (8 hex digits)"
    pass

def hexconv(test):
    try:
        if int(test, 16):
            if 0< len(test) <= 8:
                res = int(test,16)
                print("Decimal value of " + test + " is " + str(res) +".")
            else:
                raise MemoryError
        else:
            raise HexFormatError
    
    except ValueError:
        raise HexFormatError("Error occured: Not fit for Hexadecimal!")

hexconv("0xff")
