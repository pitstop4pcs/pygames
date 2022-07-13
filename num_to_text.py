def ordinal(number: int):
    """Return the ordinal of an integer in English text."""
    hundreds_string = ''
    number_string = str(number)
    units = number_string[len(number_string) - 1]
    if len(number_string) > 1:
        tens = number_string[len(number_string) - 2]
    else:
        tens = '0'
    if len(number_string) > 2:
        hundreds = number_string[len(number_string) - 3]
    else:
        hundreds = '0'
    if len(number_string) > 3:
        thousands = number_string[-6:-3]
        if int(thousands) > 0:
            thousands_string = cardinal(thousands) + ' thousand'
            if int(number_string[-3:]) != 0 and int(number_string[-3:]) > 99:
                thousands_string += ', '
    units_map = {
        0: 'th',
        1: 'First',
        2: 'Second',
        3: 'Third',
        4: 'Fourth',
        5: 'Fifth',
        6: 'Sixth',
        7: 'Seventh',
        8: 'Eighth',
        9: 'Ninth',
    }
    tens_map = {
        0: ['', ''],
        1: ['Ten', 'Eleven', 'Twelf', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'],
        2: ['Twentie', 'Twenty-', 'Twenty'],
        3: ['Thirtie', 'Thirty-', 'Thirty'],
        4: ['Fortie', 'Forty-', 'Forty'],
        5: ['Fiftie', 'Fifty-', 'Fifty'],
        6: ['Sixtie', 'Sixty-', 'Sixty'],
        7: ['Seventie', 'Seventy-', 'Seventy'],
        8: ['Eightie', 'Eighty-', 'Eighty'],
        9: ['Ninetie', 'Ninety-', 'Ninety']
    }
    if int(units) == 0:
        tens_idx = 0
    else:
        tens_idx = 1
    if int(tens) == 1:
        tens_idx = int(units)
        units = str(0)
    units_string = units_map[int(units)]
    tens_string = tens_map[int(tens)][tens_idx]
    if int(hundreds) > 0:
        hundreds_string = cardinal(int(hundreds))
        hundreds_string += ' hundred'
        if int(units) > 0 or int(units) == 0 and int(tens) != 0:
            hundreds_string += ' and '
    if len(number_string) >= 2:
        units_string = units_string.lower()
    if len(number_string) >= 3:
        tens_string = tens_string.lower()
    if len(number_string) >= 4:
        hundreds_string = hundreds_string.lower()

    return hundreds_string + tens_string + units_string


def cardinal(number: int):
    """Return an integer in English text."""
    hundreds_string = ''
    number_string = str(number)
    units = number_string[len(number_string) - 1]
    if len(number_string) > 1:
        tens = number_string[len(number_string) - 2]
    else:
        tens = '0'
    if len(number_string) > 2:
        hundreds = number_string[len(number_string) - 3]
    else:
        hundreds = '0'
    units_map = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }
    tens_map = {
        0: ['', ''],
        1: ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'],
        2: ['Twenty', 'Twenty-'],
        3: ['Thirty', 'Thirty-'],
        4: ['Forty', 'Forty-'],
        5: ['Fifty', 'Fifty-'],
        6: ['Sixty', 'Sixty-'],
        7: ['Seventy', 'Seventy-'],
        8: ['Eighty', 'Eighty-'],
        9: ['Ninety', 'Ninety-']
    }
    if int(units) == 0:
        tens_idx = 0
    else:
        tens_idx = 1
    if int(tens) == 1:
        tens_idx = int(units)
        units = str(0)
    units_string = units_map[int(units)]
    if len(number_string) > 1:
        units_string = units_string.lower()
    tens_string = tens_map[int(tens)][tens_idx]
    if len(number_string) >= 3:
        tens_string = tens_string.lower()
    if int(hundreds) > 0:
        hundreds_string = units_map[int(hundreds)]
        hundreds_string += ' hundred'
        if int(units) > 0 or int(units) == 0 and int(tens) != 0:
            hundreds_string += ' and '
    return hundreds_string + tens_string + units_string


