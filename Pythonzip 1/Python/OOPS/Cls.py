class Flight :
    def __init__(self,number) :
        if not number[:2].isalpha() :
            raise ValueError(f"No airlone code in '{number}'")
        if not number[:2].isupper() :
            raise ValueError(f"Inavlid code in '{number}'")
        if not number[2:].isdigit() :
            raise ValueError(f"Inavlid code in '{number}'")
f = Flight('RT1234')