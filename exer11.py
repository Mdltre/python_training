import re
class CardFormatError(Exception):
    "Raised if the given input does not match the pattern required."
    pass

def is_valid_credit_card_number(card_num):
    pattern = r'^[456](?!.*(\d)(?:-?\1){4})\d{3}(?:-?\d{4}){3}$'

    if not re.match(pattern, card_num):
        raise CardFormatError
    
    else:
        print("Credit card valid.")
    
is_valid_credit_card_number('4566-5693-2257-0981')