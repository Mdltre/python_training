test = "0xff"

class HexFormatError(Exception):
    "Raised if the string does not fit with the format for hexadecimal."
    pass

class MemoryError(Exception):
    "Raised if the string is beyond 4-bytes (8 hex digits)"
    pass

def hexconv(string):
    res = int(string,16)
    print("Decimal value of inputted hex is " + str(res))

try:
    if int(test, 16):
        if 0< len(test) <= 8:
            hexconv(test)
        else:
            raise MemoryError
    else:
        raise HexFormatError
    
except ValueError:
   raise HexFormatError("Error occured: Not fit for Hexadecimal!")